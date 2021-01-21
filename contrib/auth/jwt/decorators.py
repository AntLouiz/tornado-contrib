import jwt
import re
import datetime
from contrib.auth.jwt.models import RevokedToken
from contrib.auth.models import User
from tornado.web import Finish
from pay.settings import JWT_SECRET, ACCESS_TOKEN_EXPIRITY_TIME, DATABASE_NAME



def jwt_required(handler_method):

    async def inner_handler(*args, **kwargs):
        args, kwargs = await verify_handler_jwt(*args, **kwargs)

        return await handler_method(*args, **kwargs)

    return inner_handler


def create_access_token(username, algorithm='HS256'):
    token_exp = _calculate_token_expirity_time(
        seconds=ACCESS_TOKEN_EXPIRITY_TIME
    )
    body_data = {
        'username': username,
        'exp': token_exp
    }

    new_token = jwt.encode(
        body_data,
        JWT_SECRET,
        algorithm=algorithm
    )

    return new_token.decode('utf-8')


def decode_access_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    except (ValueError, jwt.exceptions.InvalidAlgorithmError):
        decoded = None

    return decoded


async def _validate_token_with_user_model(handler_object, token, check_refresh=True):
    valid_token = decode_access_token(token)

    if not valid_token:
        return _is_unauthorized(handler_object, msg='Invalid access token')

    jwt_username = valid_token.get('username')
    db_client = handler_object.settings['db_client']
    database = db_client[DATABASE_NAME]
    revoked_tokens = RevokedToken(database)
    user = User(database)

    user = await user.manager.find({'username': jwt_username, 'is_active': True})
    if not user:
        return _is_unauthorized(handler_object, msg='User not found')

    is_revoked = await revoked_tokens.manager.find_one({'jti': token})
    if is_revoked:
        return _is_unauthorized(handler_object, msg='Current token was revoked')

    if check_refresh:
        is_refresh_token = valid_token.get('refresh_token', False)

        if is_refresh_token:
            return _is_unauthorized(handler_object, msg='Invalid access token')

    user.pop('password', None)
    token_data = {
        'jwt_user': user,
        'jti': token
    }

    return token_data


async def verify_handler_jwt(*args, **kwargs):
    handler_object = args[0]

    try:
        token = _extract_token(handler_object)
        token_data = await _validate_token_with_user_model(
            handler_object,
            token
        )

        # Adicionando o jwt_user ao handler
        handler_object.jwt_user = token_data['jwt_user']
        handler_object.jti = token_data['jti']

    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError) as e:
        expired_msg = str(e)
        return _is_unauthorized(handler_object, msg=expired_msg)

    return args, kwargs


def _is_unauthorized(request_handler, msg='Access Token is missing or invalid'):
    request_handler.json_response({'error': msg}, 401)
    raise Finish()


def _extract_token(handler_object):
    token_regex = re.compile(r'^Bearer (?P<token>.+)$')

    authorization_header_value = handler_object.request.headers.get(
        'Authorization'
    )

    if not authorization_header_value:
        return _is_unauthorized(handler_object)

    match_authorization_header = token_regex.match(
        authorization_header_value
    )

    if not match_authorization_header:
        return _is_unauthorized(handler_object)

    token = match_authorization_header.group(1)
    return token


def _calculate_token_expirity_time(seconds):
    return datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds)

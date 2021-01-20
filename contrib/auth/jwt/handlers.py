import datetime
from contrib.base.handlers import CreateAPIView, RetrieveAPIView
from contrib.auth.models import User
from contrib.auth.jwt.models import RevokedToken
from contrib.auth.jwt.hash import verify_password
from contrib.auth.jwt.decorators import create_access_token
from contrib.auth.jwt.authenticators import JwtAuthentication


class JWTLoginHandler(CreateAPIView):
    model = User

    async def post(self, *args, **kwargs):
        data = self.get_body_data()

        try:
            username = data['username']
            password = data['password']
        except KeyError:
            error_msg = {'error': 'Insert the username and password.'}
            return self.json_response(data=error_msg, status=400)

        queryset = await self.model.manager.find({'username': username}, many=False)
        if not queryset.total:
            error_msg = {'error': 'Username or password invalid.'}
            return self.json_response(data=error_msg, status=401)

        user = queryset.asdict()

        encrypted_password = user.get('password')
        password_is_valid = verify_password(password, encrypted_password)
        if not password_is_valid:
            error_msg = {'error': 'Username or password invalid.'}
            return self.json_response(data=error_msg, status=401)

        access_token = create_access_token(username)
        now = datetime.datetime.utcnow()

        query_filter = {'_id': user['_id']}
        data = {'last_login': now.isoformat()}
        self.model.manager.update(query_filter, data=data)

        response_data = {'access_token': access_token}
        return self.json_response(response_data, status=200)


class JWTLogoutHandler(RetrieveAPIView):
    model = RevokedToken
    authentication_class = JwtAuthentication

    async def get(self, *args, **kwargs):
        jti = self.jti

        queryset = await self.model.manager.find({"jti": jti})
        if queryset.total != 0:
            return self.json_response({'error': 'Current token is revoked.'}, 401)

        token = self.model(raw_data={'jti': jti})
        await self.model.manager.create(token)

        data = {
            'message': 'Token revogado'
        }

        self.json_response(data)
        return


class JWTRefreshHandler():
    pass

class CurrentJWTUser():
    pass

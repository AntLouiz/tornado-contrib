import datetime
from contrib.base.handlers import CreateAPIView
from contrib.auth.models import User
from contrib.auth.jwt.hash import verify_password
from contrib.auth.jwt.decorators import create_access_token


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

class JWTLogoutHandler():
    pass

class JWTRefreshHandler():
    pass

class CurrentJWTUser():
    pass

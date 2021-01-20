import datetime
from contrib.base.handlers import ModelAPIView
from contrib.auth.models import Permission, User
from contrib.auth.jwt.hash import hash_password
from core.models import Person, Customer
from contrib.auth.jwt.authenticators import JwtAuthentication
from pymongo import ASCENDING


class PersonModelAPIView(ModelAPIView):
    model = Person
    lookup_field = '_id'
    # authentication_class = JwtAuthentication
    lookup_url_kwarg = 'object_id'

    async def get_queryset(self, many=True, *args, **kwargs):
        sort_rule = ('name', ASCENDING)
        queryset = await self.model.manager.find(
            self.query_filter,
            many=many,
            sort=sort_rule
        )
        return queryset


class UserModelAPIView(ModelAPIView):
    model = User
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'

    async def post(self, *args, **kwargs):
        data = self.get_body_data()
        username = data['username']

        queryset = await self.model.manager.find({'username': username})
        if queryset.total:
            return self.json_response({'error': "Username already exists."}, 400)

        password = data.get('password')
        try:
            password = password.encode('utf-8').decode('utf-8')
            password = hash_password(password)
            data['password'] = password

        except Exception:
            return self.json_response({'error': "Wrong password sequence."}, 400)

        date_joined = datetime.datetime.utcnow()
        data['date_joined'] = date_joined

        model_object = self.model(data)
        await self.model.manager.create(model_object)

        response = model_object.to_primitive(role='public')
        return self.json_response(response, status=201)


class CustomerModelAPIView(ModelAPIView):
    model = Customer
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'


class PermissionModelAPIView(ModelAPIView):
    model = Permission
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'

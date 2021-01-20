from base.models import MongoModel
from schematics.types import (
    StringType,
    ModelType,
    BooleanType,
    ListType,
)


class Permission(MongoModel):
    name = StringType()
    codename = StringType()

    class Meta:
        collection_name = 'permissions'


class Group(MongoModel):
    name = StringType()
    permissions = ListType(ModelType(Permission))

    class Meta:
        collection_name = 'groups'


class User(MongoModel):
    """
    https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
    """
    username = StringType()
    first_name = StringType()
    last_name = StringType()
    email = StringType()
    password = StringType()
    groups = ListType(ModelType(Group))
    permissions = ListType(ModelType(Permission))
    is_staff = BooleanType()
    is_active = BooleanType()
    is_superuser = BooleanType()
    last_login = UTCDatetimeType()
    date_joined = UTCDatetimeType()

    class Meta:
        collection_name = 'users'

    def get_username(self):
        pass
    
    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    def set_password(raw_password):
        pass

    def check_password(raw_password):
        pass

    def get_user_permissions(obj=None):
        pass

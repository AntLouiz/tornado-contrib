from base.models import MotorModel
from base.fields import (
    StringType,
    ModelType,
    BooleanType,
    ListType,
    UTCDateTimeType
)
from schematics.transforms import blacklist


class Permission(MotorModel):
    name = StringType()
    codename = StringType()

    class Meta:
        collection_name = 'permissions'


class Group(MotorModel):
    name = StringType()
    permissions = ListType(ModelType(Permission))

    class Meta:
        collection_name = 'groups'


class User(MotorModel):
    """
    https://docs.djangoproject.com/en/3.1/ref/contrib/auth/
    """

    username = StringType(required=True)
    first_name = StringType(required=True)
    last_name = StringType()
    email = StringType(required=True)
    password = StringType(required=True)
    groups = ListType(ModelType(Group))
    permissions = ListType(ModelType(Permission))
    is_staff = BooleanType()
    is_active = BooleanType(default=True)
    is_superuser = BooleanType(default=False)
    last_login = UTCDateTimeType()
    date_joined = UTCDateTimeType()

    class Meta:
        collection_name = 'users'

    class Options:
        roles = {'public': blacklist('password')}

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

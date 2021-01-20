from core.handlers import (
    UserModelAPIView,
    PersonModelAPIView,
    CustomerModelAPIView,
    PermissionModelAPIView,
)
from contrib.auth.jwt.handlers import JWTLoginHandler, JWTLogoutHandler


urlpatterns = [
    (r"/login/", JWTLoginHandler),
    (r"/logout/", JWTLogoutHandler),
    (r"/users/(?P<object_id>[0-9a-fA-F]{24})*", UserModelAPIView),
    (r"/persons/(?P<object_id>[0-9a-fA-F]{24})*", PersonModelAPIView),
    (r"/customers/(?P<object_id>[0-9a-fA-F]{24})*", CustomerModelAPIView),
    (r"/permissions/(?P<object_id>[0-9a-fA-F]{24})*", PermissionModelAPIView)
]

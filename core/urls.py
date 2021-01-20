from core.handlers import (
    PersonModelAPIView,
    CustomerModelAPIView,
    PermissionModelAPIView,
)


urlpatterns = [
    (r"/persons/(?P<object_id>[0-9a-fA-F]{24})*", PersonModelAPIView),
    (r"/customers/(?P<object_id>[0-9a-fA-F]{24})*", CustomerModelAPIView),
    (r"/permissions/(?P<object_id>[0-9a-fA-F]{24})*", PermissionModelAPIView)
]

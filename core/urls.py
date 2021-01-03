from core.handlers import PersonModelAPIView


urlpatterns = [
    (r"/persons/(?P<object_id>[0-9a-fA-F]{24})*", PersonModelAPIView),
]

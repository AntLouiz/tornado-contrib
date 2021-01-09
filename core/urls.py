from core.handlers import PersonModelAPIView, CustomerModelAPIView


urlpatterns = [
    (r"/persons/(?P<object_id>[0-9a-fA-F]{24})*", PersonModelAPIView),
    (r"/customers/(?P<object_id>[0-9a-fA-F]{24})*", CustomerModelAPIView),
]

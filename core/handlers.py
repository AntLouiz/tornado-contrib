from base.handlers import ModelAPIView
from core.models import Person


class PersonModelAPIView(ModelAPIView):
    model = Person
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'

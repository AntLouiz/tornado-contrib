from contrib.base.handlers import ModelAPIView
from core.models import Person, Customer
from pymongo import ASCENDING


class PersonModelAPIView(ModelAPIView):
    model = Person
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'

    async def get_queryset(self, many=True, *args, **kwargs):
        sort_rule = ('name', ASCENDING)
        queryset = await self.model.manager.find(
            self.query_filter,
            many=many,
            sort=sort_rule
        )
        return queryset


class CustomerModelAPIView(ModelAPIView):
    model = Customer
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'

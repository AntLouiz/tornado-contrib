from base.handlers import ModelAPIView
from core.models import Person, Customer


class PersonModelAPIView(ModelAPIView):
    model = Person
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'

    async def list(self, *args, **kwargs):
        queryset = await self.get_queryset(*args, **kwargs)
        response = self.process_response(queryset)

        customer = Customer(self.db)

        print(await customer.manager.find())

        response = self.paginate_response(queryset)
        return self.json_response(data=response)


class CustomerModelAPIView(ModelAPIView):
    model = Customer
    lookup_field = '_id'
    lookup_url_kwarg = 'object_id'

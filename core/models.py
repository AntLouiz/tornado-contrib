from contrib.base.models import MongoModel
from contrib.base.fields import StringType, ModelType


class Customer(MongoModel):
    name = StringType()

    class Meta:
        collection_name = 'customers'


class Person(MongoModel):
    name = StringType()
    customer = ModelType(Customer)

    class Meta:
        collection_name = 'persons'

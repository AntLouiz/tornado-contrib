from base.models import MongoModel
from schematics.types import StringType, ModelType


class Customer(MongoModel):
    name = StringType()

    class Meta:
        collection_name = 'customers'


class Person(MongoModel):
    name = StringType()
    customer = ModelType(Customer)

    class Meta:
        collection_name = 'persons'

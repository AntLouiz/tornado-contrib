from base.models import MongoModel
from schematics.types import StringType


class Person(MongoModel):
    name = StringType()

    class Meta:
        collection_name = 'persons'

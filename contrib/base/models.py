from schematics.types import StringType
from schematics.models import Model
from schematics.exceptions import DataError
from .managers import MongoModelManager
from motor import MotorDatabase


class MongoModel(Model):
    _manager = MongoModelManager

    def __init__(self, raw_data=None, *args, **kwargs):
        self.manager = MongoModelManager

        if isinstance(raw_data, MotorDatabase):
            db = raw_data
            collection_name = self.Meta.collection_name
            collection = db[collection_name]
            self.manager = MongoModelManager(collection)
            raw_data = None

        kwargs['strict'] = False
        super().__init__(raw_data, *args, **kwargs)

    def is_valid(self, raise_exception=False):
        if raise_exception:
            super().validate()

        try:
            super().validate()
            is_valid = True
        except DataError as e:
            is_valid = False

        return is_valid

    @classmethod
    def get_protected_fields(cls):
        return ['_id']

    class Meta:
        collection_name = 'base'

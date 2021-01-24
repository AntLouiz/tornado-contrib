from schematics.types import StringType
from schematics.models import Model
from schematics.exceptions import DataError
from .managers import MotorModelManager
from motor import MotorDatabase
from motor.motor_asyncio import AsyncIOMotorDatabase


class MotorModel(Model):
    _manager = MotorModelManager

    def __init__(self, raw_data=None, *args, **kwargs):
        self.manager = MotorModelManager

        if isinstance(raw_data, MotorDatabase) or isinstance(raw_data, AsyncIOMotorDatabase):
            db = raw_data
            collection_name = self.Meta.collection_name
            collection = db[collection_name]
            self.manager = MotorModelManager(collection)
            raw_data = None

        # kwargs['strict'] = False
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

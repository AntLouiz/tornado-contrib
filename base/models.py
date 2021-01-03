from schematics.types import StringType
from schematics.models import Model
from schematics.exceptions import DataError
from .managers import MongoModelManager


class MongoModel(Model):
    _manager = MongoModelManager

    def __init__(self, *args, **kwargs):
        self.manager = MongoModelManager
        kwargs['strict'] = False
        super().__init__(*args, **kwargs)

    def is_valid(self, raise_exception=False):
        if raise_exception:
            super().validate()

        try:
            super().validate()
            is_valid = True
        except DataError as e:
            is_valid = False

        return is_valid

    class Meta:
        collection_name = 'base'

import bson
from schematics.types import *
from schematics.common import *
from schematics.exceptions import ConversionError
from schematics.contrib.mongo import ObjectIdType


class ObjectIdType(ObjectIdType):

    def to_native(self, value, context=None):
        if not isinstance(value, bson.objectid.ObjectId) or not isinstance(value, str):
            try:
                value = bson.objectid.ObjectId(str(value))
            except bson.objectid.InvalidId:
                try:
                    value = value['$oid']
                except KeyError:
                    raise ConversionError(self.messages['convert'])
        return value

from contrib.base.models import MongoModel
from contrib.base.fields import StringType



class RevokedToken(MongoModel):
    jti = StringType(max_length=250, required=True)

    class Meta:
        collection_name = 'revoked_tokens'

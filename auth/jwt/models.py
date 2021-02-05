from contrib.base.models import MotorModel
from contrib.base.fields import StringType



class RevokedToken(MotorModel):
    jti = StringType(max_length=250, required=True)

    class Meta:
        collection_name = 'revoked_tokens'

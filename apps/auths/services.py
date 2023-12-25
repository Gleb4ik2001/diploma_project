from . import models
import jwt
import datetime
from django.conf import settings



def create_token(user_id:int)->str:
    payload = dict(
        id= user_id,
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=2),
        iat = datetime.datetime.utcnow()
    )
    token = jwt.encode(payload , settings.JWT_SECRET_KEY,algorithm='HS256')
    return token
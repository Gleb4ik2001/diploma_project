import dataclasses
from typing import TYPE_CHECKING
from . import models
import jwt
import datetime
from django.conf import settings
from .models import CustomUser

if TYPE_CHECKING:
    from .models import CustomUser

    

def user_email_selector(email:str)->'CustomUser':
    user = CustomUser.objects.filter(email=email).first()
    return user

def create_token(user_id:int)->str:
    payload = dict(
        id= user_id,
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=2),
        iat = datetime.datetime.utcnow()
    )
    token = jwt.encode(payload , settings.JWT_SECRET_KEY,algorithm='HS256')
    return token
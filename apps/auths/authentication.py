from django.conf import settings
from rest_framework import authentication,exceptions
import jwt

from .models import CustomUser
from rest_framework.request import Request


class CustomUserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request:Request):
        token = request.COOKIES.get('jwt')
        if not token:
            return None
        try:
            payload = jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed('Unathorized')
        user = CustomUser.objects.filter(id=payload['id']).first()

        return (user , None)
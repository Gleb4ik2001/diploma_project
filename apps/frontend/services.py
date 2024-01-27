import jwt
from django.http.request import HttpRequest
from django.http.response import HttpResponse ,HttpResponseBadRequest
from django.conf import settings
from django.contrib.auth import get_user_model


def get_user_model_custom(request:HttpRequest)->HttpResponse:
    jwt_token = request.COOKIES.get('jwt')
    try:
        payload = jwt.decode(jwt_token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        user_id = payload['id']
    except jwt.ExpiredSignatureError:
        return HttpResponseBadRequest('Token has expired')
    except jwt.InvalidTokenError:
        return HttpResponseBadRequest('Invalid token')
    User = get_user_model()
    user = User.objects.get(pk=user_id)
    return user 
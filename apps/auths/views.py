from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrateUserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import (
    authenticate,
    login
)
from rest_framework.response import Response
from rest_framework import exceptions
from django.contrib.auth.hashers import make_password
from . import services
from .authentication import CustomUserAuthentication

class JobSeekerRegistrateAPI(APIView):

    def post(self, request):
        try:
            serializer = RegistrateUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Error:', e)
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class LoginAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            raise exceptions.AuthenticationFailed('Данные введены неправильно')

        user = services.user_email_selector(email=email)
        if user is None:
            raise exceptions.AuthenticationFailed('Данные введены неправильно')

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Данные введены неправильно')

        token = services.create_token(user.id)
        resp = Response()
        resp.set_cookie(key='jwt', value=token, httponly=True)
        resp.data = {'message': 'Вы успешно вошли в систему'}
        return resp
    
class UserApi(APIView):
    authentication_classes =(CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        user = request.user
        serializer= RegistrateUserSerializer(user)
        return Response(serializer.data)
    
class UserLogoutAPI(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        resp = Response()
        resp.delete_cookie('jwt')
        resp.data = {'message':"you logout"}
        return resp
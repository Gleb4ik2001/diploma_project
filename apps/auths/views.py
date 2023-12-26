from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    RegistrateUserSerializer,
    RegistrateCompanySerializer  ,
    UpdateUserSerializer,
    AllUserDataSerializer
)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import (
    authenticate,
    login
)
from rest_framework import generics
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
    

class CompanyRegistrateAPI(APIView):

    def post(self, request):
        try:
            serializer = RegistrateCompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Company registered successfully'}, status=status.HTTP_201_CREATED)
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
        serializer= AllUserDataSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = UpdateUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateUserProfileView(generics.UpdateAPIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
class UserLogoutAPI(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        resp = Response()
        resp.delete_cookie('jwt')
        resp.data = {'message':"you logout"}
        return resp
    

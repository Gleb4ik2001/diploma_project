from typing import Optional
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

from.filters import VacancyFilter
from .models import (
    CurriculumVitae,
    Vacancy,
    CategoryChoices,
    VacancyResponses
)
from .serializers import (
    CurriculumVitaeSerializer,
    VacancySerializer,
    CategoryChoicesSerializer,
    VacancyResponsesSerializer
)
from rest_framework.status import(
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# ------------------------------------
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import permissions
from auths.authentication import CustomUserAuthentication
from rest_framework import status
from .permissions import IsOwnerOfVacancyPermission
from django_filters.rest_framework import DjangoFilterBackend

class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (CustomUserAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None, *args, **kwargs):
        try:
            cv = self.queryset.get(id=pk)
        except CurriculumVitae.DoesNotExist:
            return Response(
                data={
                    'status':'bad',
                    'message':'object does not exists'
                },
                status=400
            )
        serializer = self.get_serializer(cv)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user) 
        return Response(serializer.data, status=201)

    def update(self, request,pk=None, *args, **kwargs):
        # Метод для обновления существующего резюме
        try:
            cv = self.queryset.get(id=pk)
        except CurriculumVitae.DoesNotExist:
            return Response(
                data={
                    'status':'bad',
                    'message':'object does not exists'
                },
                status=400
            )
        serializer = self.get_serializer(cv, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request,pk=None, *args, **kwargs):
        # Метод для частичного обновления существующего резюме
        try:
            instance = self.queryset.get(id=pk)
        except CurriculumVitae.DoesNotExist:
            return Response(
                data={
                    'status':'bad',
                    'message':'object does not exists'
                },
                status=400
            )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request,pk=None, *args, **kwargs):
        # Метод для удаления резюме
        try:
            instance = self.queryset.get(id=pk)
        except CurriculumVitae.DoesNotExist:
            return Response(
                data={
                    'status':'bad',
                    'message':'object does not exists'
                },
                status=400
            )
        instance.delete()
        return Response(
            data={
                'status':"deleted"
            }
        )
    


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilter
    


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOfVacancyPermission()]
        return [permissions.AllowAny()] 

    def list(self, request:Request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk, *args, **kwargs):
        # Получение одной вакансии по ее идентификатору
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.user.is_company:
            return Response(
                {
                    'detail': 'Only companies can create vacancies.'
                },
                  status=status.HTTP_403_FORBIDDEN
            )
        # Создание новой вакансии
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=request.user)  # Присваиваем текущую компанию
        return Response(serializer.data, status=201)

    def update(self, request,pk, *args, **kwargs):
        # Обновление существующей вакансии
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        # Частичное обновление существующей вакансии
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # Удаление вакансии
        instance = self.get_object()
        instance.delete()
        return Response(status=204)
    
class CategoryApi(viewsets.ViewSet):
    queryset = CategoryChoices.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (CustomUserAuthentication,)


    def list(self, request: Request,*args,**kwargs) -> Response:
        serializer = CategoryChoicesSerializer(instance=self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self,pk:int, request: Request,) -> Response:
        category = self.queryset.get(id=pk)
        serializer = CategoryChoicesSerializer(instance=category,)
        return Response(serializer.data)
    

class VacancyResponsesViewset(viewsets.ModelViewSet):

    queryset= VacancyResponses
    serializer_class = VacancyResponsesSerializer
    authentication_classes = (CustomUserAuthentication)

    def list(self,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

    def retrieve(self,pk:int, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)

    def update(self,pk:int, request, *args, **kwargs):
        # Обновление существующей вакансии
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        # Частичное обновление существующей вакансии
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # Удаление вакансии
        instance = self.get_object()
        instance.delete()
        return Response(status=204)
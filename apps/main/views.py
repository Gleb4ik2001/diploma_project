from typing import Optional
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import (
    CurriculumVitae,
    Vacancy
)
from .serializers import (
    CurriculumVitaeSerializer,
    VacancySerializer,
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

class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer


    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        elif self.action in ['retrieve','update','partial_update','destroy','create']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]  # Разрешение по умолчанию
        

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None, *args, **kwargs):
        # Метод для получения одного резюме по его идентификатору
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
        # Метод для создания нового резюме
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)  # Присваиваем текущего пользователя
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
    permission_classes = [permissions.IsAuthenticated]  # Или другие разрешения по вашему выбору

    def list(self, request, *args, **kwargs):
        # Получение списка всех вакансий
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # Получение одной вакансии по ее идентификатору
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Создание новой вакансии
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=request.user)  # Присваиваем текущую компанию
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
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
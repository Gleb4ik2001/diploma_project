from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from .models import (
    CurriculumVitae,
    Vacancy
)
from .serializers import (
    CurriculumVitaeSerializer,
    VacancySerializer
)
from rest_framework.status import(
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)



class RezumeViewSet(ViewSet):
    queryset = CurriculumVitae.objects.all()
    def list(self,request:Request)->Response:
        serializer =CurriculumVitaeSerializer(
            self.queryset,
            many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(self,request:Request,pk:int)->Response:
        try:
            cv = self.queryset.get(id=pk)
        except CurriculumVitae.DoesNotExist:
            return Response(
                data={
                    'status':'bad',
                    'message':f'no data with ID {pk}'
                    },
                status=HTTP_404_NOT_FOUND
            )
        serializer = CurriculumVitaeSerializer(
            instance=cv
        )
        return Response(
            data=serializer.data,
            status=HTTP_200_OK
        )

    
class VacancyViewSet(ViewSet):
    queryset = Vacancy.objects.all()

    def list(self,request:Request,*args,**kwargs):
        serializer = VacancySerializer(instance=self.queryset,many=True)
        return Response(
            data=serializer.data
        )
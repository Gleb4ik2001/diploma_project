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
# ------------------------------------
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)



class RezumeViewSet(ViewSet):
    queryset = CurriculumVitae.objects.all()
    permission_classes =[IsAuthenticated]
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
    
# Views html
class RegistraionView(View):
    template = 'registrate.html'
    def post(self,request:HttpRequest)->HttpResponse:
        return 
    
    def get(self,request:HttpRequest)->HttpResponse:
        return render(request=request,template_name=self.template,context={})
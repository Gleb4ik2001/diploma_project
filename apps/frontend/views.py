from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.http.request import HttpRequest


class JobSeekerRegistrateView(View):
    """Класс для представлений HTML щаблонов для регистрации соискателя"""

    temaplate_name = 'user_registrate.html'

    def get(self,request:HttpRequest)->HttpResponse:
        return render(
            request=request,
            template_name=self.temaplate_name,
            context={}
        )

    def post(self,request:HttpRequest)->HttpResponse:
        pass

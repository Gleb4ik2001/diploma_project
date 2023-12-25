from django.shortcuts import render ,redirect
from django.views import View
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from .forms import (
    JobSeekerRegistrationForm,
    LoginForm
)
from auths.models import (
    CustomUser
)
from django.conf import settings
import jwt
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest


class JobSeekerRegistrateView(View):
    """Класс для представлений HTML щаблонов для регистрации соискателя"""

    temaplate_name = 'user_registrate.html'
    
    def get(self,request:HttpRequest)->HttpResponse:
        return render(
            request=request,
            template_name=self.temaplate_name,
            context={
            }
        )

class CompanyRegistrateView(View):
    """Класс для представлений HTML щаблонов для регистрации соискателя"""

    temaplate_name = 'company_registrate.html'
    
    def get(self,request:HttpRequest)->HttpResponse:
        return render(
            request=request,
            template_name=self.temaplate_name,
            context={
            }
        )


class LoginView(View):
    """Класс для представлений HTML щаблонов для регистрации соискателя"""

    temaplate_name = 'login.html'
    
    def get(self,request:HttpRequest)->HttpResponse:
        form = LoginForm()
        return render(
            request=request,
            template_name=self.temaplate_name,
            context={
                'form':form
            }
        )

class JobSeekerMainView(TemplateView):
    template_name = 'jobseeker_main.html'
    company_template_name = 'company_main.html'

    def get(self, request, *args, **kwargs):
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

        if user.is_company:
            return render(request, self.company_template_name, {'user': user})
        else:
            return render(request, self.template_name, {'user': user})
        
class UserProfileView(View):
    template_name = 'me.html'
    def get(self, request,*args,**kwargs):
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
        return render(
            request=request,
            template_name=self.template_name,
            context={'user':user}
        )
    
class CategoryDetailView(View):
    template_name = 'category_detail.html'
    def get(self,pk,request)->HttpResponse:
        
        return render(
            request=request,
            template_name=self.template_name,
            context={}
        )
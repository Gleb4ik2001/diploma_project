from django.shortcuts import render ,redirect
from django.views import View
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from .forms import (
    JobSeekerRegistrationForm,
    LoginForm
)
from auths.models import (
    CustomUserManager,
    CustomUser
)


class JobSeekerRegistrateView(View):
    """Класс для представлений HTML щаблонов для регистрации соискателя"""

    temaplate_name = 'user_registrate.html'
    
    def get(self,request:HttpRequest)->HttpResponse:
        form = JobSeekerRegistrationForm()
        return render(
            request=request,
            template_name=self.temaplate_name,
            context={
                'form':form
            }
        )

    def post(self,request:HttpRequest)->HttpResponse:
        form = JobSeekerRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            return HttpResponse(user)

        return render(request, self.temaplate_name, {'form': form})


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

class JobSeekerMainView(View):
    template_name = 'jobseeker_main.html'

    def get(self,request:HttpRequest)->HttpRequest:
        user = request.user
        return render(
            request=request,
            template_name=self.template_name,
            context={"user":user}
        )
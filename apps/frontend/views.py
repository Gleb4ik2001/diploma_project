from django.shortcuts import render ,redirect
from django.views import View
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib import messages
from .forms import (
    LoginForm,
    CurriculumVitaeForm,
    VacancyForm
)
from auths.models import (
    CustomUser
)
from main.models import (
    CategoryChoices,
    Vacancy,
    CurriculumVitae
)
from django.views.generic.detail import DetailView
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

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        try:
            category = CategoryChoices.objects.get(slug=slug)
        except CategoryChoices.DoesNotExist:
            raise HttpResponse("Такой категории не существует")
        vacancys = Vacancy.objects.filter(category=category)
        user = request.user
        context = {
            'vacancys': vacancys,
            'category':category,
            'user':user
        }
        return render(request, self.template_name, context)
    
class VacancyView(View):
    template_name = 'vacancy_detail.html'

    def get(self,request:HttpRequest,pk)->HttpResponse:
        vacancy = Vacancy.objects.get(id=pk)
        user = request.user
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'vacancy':vacancy,
                'user':user
            }
        )
    
class CVView(View):
    template_name ='cv.html'
    def get(self,request:HttpRequest)->HttpResponse:
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
        cvs = CurriculumVitae.objects.filter(user = user)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user':user,
                'cvs':cvs
            }
        )
        
class CVDetailView(View):
    template_name = 'cv_detail.html'

    def get(self,request,pk):
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
        cv = CurriculumVitae.objects.get(id=pk)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user':user,
                'cv':cv
            }
        )


        
class MyVacancysView(View):
    template_name = 'my_vacancys.html'

    def get(self,request:HttpRequest)->HttpResponse:
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
        vacancies = Vacancy.objects.filter(company=user)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user':user,
                'vacancys':vacancies
            }
        )

class MyVacancyDetailView(View):
    template_name=  'my_vacancy_detail.html'

    def get(self,request:HttpRequest,pk)->HttpResponse:
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
        vacancy= Vacancy.objects.get(id=pk)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'user':user,
                'vacancy':vacancy
            }
        )
    

class MakeVacancyiew(View):
    template_name = 'make_vacancy.html'

    def get(self, request):
        form = VacancyForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
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
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = user
            vacancy.save()
            messages.success(request, 'Резюме успешно создано!')
            return redirect('my_vacancys')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            return render(request, self.template_name, {'form': form})
        
class MakeCVView(View):
    template_name = 'make_cv.html'

    def get(self, request):
        form = CurriculumVitaeForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
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
        form = CurriculumVitaeForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = user
            cv.save()
            messages.success(request, 'Резюме успешно создано!')
            return redirect('cv_view')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            return render(request, self.template_name, {'form': form})
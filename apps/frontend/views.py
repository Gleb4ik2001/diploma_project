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
from .services import get_user_model_custom


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
        try:
            user = get_user_model_custom(request)
        except AttributeError as ex:
            redirect('login')
        if user.is_company:
            return render(request, self.company_template_name, {'user': user})
        else:
            return render(request, self.template_name, {'user': user})
        
class UserProfileView(View):
    template_name = 'me.html'
    def get(self, request,*args,**kwargs):
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
        if user.is_company== False:
            return HttpResponse('У вас нет прав доступа для этой страницы')
        form = VacancyForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        user = get_user_model_custom(request)
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
        user = get_user_model_custom(request)
        if user.is_company:
            return HttpResponse('Компания не может создать резюме')
        form = CurriculumVitaeForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        user = get_user_model_custom(request)
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
        
    
def test_fetches(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='test_fetch.html',
        context={}
    )
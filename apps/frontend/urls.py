from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    JobSeekerRegistrateView,
    CompanyRegistrateView,
    LoginView,
    JobSeekerMainView,
    UserProfileView,
    CategoryDetailView,
    VacancyView,
    CVView,
    CVDetailView,
    MakeCVView,
    MyVacancysView,
    MyVacancyDetailView,
    MakeVacancyiew,
    test_fetches
)


urlpatterns = [
    path('user_registrate/',JobSeekerRegistrateView.as_view(),name='user_registration'),
    path('company_registrate/',CompanyRegistrateView.as_view(),name='company_registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('main-page/',JobSeekerMainView.as_view(),name='js_main_view'),
    path('me/',UserProfileView.as_view(),name='user_profile_view'),
    path('categorys/<slug:slug>/',CategoryDetailView.as_view(),name='category_detail_view'),
    path('vacancy/<int:pk>/',VacancyView.as_view(),name='vacancy_detail_view'),
    path('my_cvs/',CVView.as_view(),name='cv_view'),
    path('cv/<int:pk>/',CVDetailView.as_view(),name='cv_detail'),
    path('cv/<int:pk>/',CVDetailView.as_view(),name='cv_detail'),
    path('make_cv/',MakeCVView.as_view(),name='make_cv'),
    path('my_vacancys/',MyVacancysView.as_view(),name='my_vacancys'),
    path('my_vacancys/<int:pk>',MyVacancyDetailView.as_view(),name='my_vacancy_detail'),
    path('make_vacancy/',MakeVacancyiew.as_view(),name='make_vacancy'),
    path('make_vacancy/',MakeVacancyiew.as_view(),name='make_vacancy'),
    path('test_fetches/',test_fetches,name='fetches')

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

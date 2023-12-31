from django.urls import path,include
from .views import (
    CurriculumVitaeViewSet,
    VacancyViewSet,
    CategoryApi
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cv',CurriculumVitaeViewSet,basename='cv_viewset')
router.register(r'vacancy',VacancyViewSet,basename='vacancy_viewset')
router.register(r'categorys',CategoryApi,basename='category_viewset')

urlpatterns = [
    path('',include(router.urls)),
]
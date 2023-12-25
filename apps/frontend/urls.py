from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    JobSeekerRegistrateView,
    CompanyRegistrateView,
    LoginView,
    JobSeekerMainView,
    UserProfileView,
    CategoryDetailView
)


urlpatterns = [
    path('user_registrate/',JobSeekerRegistrateView.as_view(),name='user_registration'),
    path('company_registrate/',CompanyRegistrateView.as_view(),name='company_registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('main-page/',JobSeekerMainView.as_view(),name='js_main_view'),
    path('me/',UserProfileView.as_view(),name='user_profile_view'),
    path('categorys/<int:pk>/',CategoryDetailView.as_view(),name='category_detail_view')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

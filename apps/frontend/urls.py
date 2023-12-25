from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    JobSeekerRegistrateView,
    LoginView    
)


urlpatterns = [
    path('user_registrate/',JobSeekerRegistrateView.as_view(),name='user_registration'),
    path('login/',LoginView.as_view(),name='login')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

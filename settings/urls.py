from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('auths.urls'),name='auths'),
    path('main/api/',include('main.urls'),name='main_urls'),
    path('',include('frontend.urls'),name='frontend')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

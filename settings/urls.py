from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from auths.views import (
    RezumeViewSet,
    VacancyViewSet
)

router = DefaultRouter()
router.register(r'cv',RezumeViewSet,basename='rezume')
router.register(r'vacancy',VacancyViewSet,basename='vacancy')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls), name='game')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

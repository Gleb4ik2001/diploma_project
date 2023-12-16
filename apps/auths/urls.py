from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main.views import RegistraionView


urlpatterns = [
    path('user_registrate/',RegistraionView.as_view(),name='registrate_user')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

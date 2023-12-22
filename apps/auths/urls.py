from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import JobseekerRegistrationAPIView

urlpatterns = [
    path('api/jobseeker_register/', JobseekerRegistrationAPIView.as_view(), name='job_seeker_registration'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
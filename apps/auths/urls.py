from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import (
    JobSeekerRegistrateAPI,
    CompanyRegistrateAPI,
    LoginAPI,
    UserApi,
    UserLogoutAPI,
    UpdateUserProfileView

)

urlpatterns = [
    path('api/jobseeker_register/', JobSeekerRegistrateAPI.as_view(), name='job_seeker_registration'),
    path('api/company_register/', CompanyRegistrateAPI.as_view(), name='company_registration'),
    path('api/login/', LoginAPI.as_view(), name='login_api'),
    path('api/me/', UserApi.as_view(), name='me'),
    path('api/me/update/', UpdateUserProfileView.as_view(), name='update_user_profile'),
    path('api/logout/', UserLogoutAPI.as_view(), name='logout_api')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )

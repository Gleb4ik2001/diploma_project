from django.contrib import admin
from .models import (
    CustomUser,
    JobSeeker,
    Company,
)


admin.site.register(CustomUser)
admin.site.register(JobSeeker)
admin.site.register(Company)
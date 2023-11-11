from django.contrib import admin
from .models import (
    CustomUser,
    CurriculumVitae,
    Languages
)


admin.site.register(CustomUser)
admin.site.register(CurriculumVitae)
admin.site.register(Languages)

from django.contrib import admin
from .models import (
    CustomUser,
    CurriculumVitae,
    Language,
    Vacancy
)


admin.site.register(CustomUser)
admin.site.register(CurriculumVitae)
admin.site.register(Language)
admin.site.register(Vacancy)
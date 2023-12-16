from django.contrib import admin
from .models import (
    CurriculumVitae,
    Language,
    Vacancy
)

admin.site.register(CurriculumVitae)
admin.site.register(Language)
admin.site.register(Vacancy)
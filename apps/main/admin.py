from django.contrib import admin
from .models import (
    CurriculumVitae,
    Language,
    Vacancy,
    VacancyResponses
)

admin.site.register(CurriculumVitae)
admin.site.register(Language)
admin.site.register(Vacancy)
admin.site.register(VacancyResponses)
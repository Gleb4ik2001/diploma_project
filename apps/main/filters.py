from django_filters import (
    CharFilter,
    FilterSet
)
from .models import Vacancy
from django.db.models.functions import Lower


class VacancyFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = {
            'title': ['icontains']
        }
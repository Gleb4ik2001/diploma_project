from rest_framework.serializers import ModelSerializer
from .models import (
    CurriculumVitae,
    Language,
    Vacancy
)
from auths.models import CustomUser, JobSeeker
from rest_framework import serializers

class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['id', 'email', 'first_name', 'last_name']

class CurriculumVitaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumVitae
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
        
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
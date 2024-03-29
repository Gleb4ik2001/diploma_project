from rest_framework.serializers import ModelSerializer
from .models import (
    CurriculumVitae,
    Language,
    Vacancy,
    CategoryChoices,
    VacancyResponses
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
    company = serializers.CharField(source='company.company_name')
    class Meta:
        model = Vacancy
        fields = '__all__'
        
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
    
class CategoryChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryChoices
        fields = '__all__'

class VacancyResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyResponses
        fields ='__all__'
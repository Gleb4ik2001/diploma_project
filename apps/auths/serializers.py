from rest_framework.serializers import ModelSerializer
from .models import (
    CurriculumVitae,
    Language,
    Vacancy,
    CustomUser
)
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =('email',)

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class CurriculumVitaeSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    languages = LanguageSerializer(many=True)
    class Meta:
        model = CurriculumVitae
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    company = CustomUserSerializer()
    class Meta:
        model = Vacancy
        fields ='__all__'

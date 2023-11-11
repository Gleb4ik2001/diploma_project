from rest_framework.serializers import ModelSerializer
from .models import (
    CurriculumVitae,
    Languages
)
from rest_framework import serializers


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'

class CurriculumVitaeSerializer(ModelSerializer):
    user = serializers.StringRelatedField()
    languages = LanguageSerializer(many=True)
    class Meta:
        model = CurriculumVitae
        fields = '__all__'
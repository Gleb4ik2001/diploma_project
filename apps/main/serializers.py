from rest_framework.serializers import ModelSerializer
from .models import (
    CurriculumVitae,
    Language,
    Vacancy
)
from auths.models import CustomUser
from rest_framework import serializers


class RegiStrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only = True
    )
    token= serializers.CharField(
        max_length = 255,
        read_only = True
    )

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'password',
            'token'
        ]



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

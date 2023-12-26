from rest_framework import serializers
from .models import CustomUser
from . import services

class RegistrateUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only = True)
    def create(self, validated_data):
        user = CustomUser.objects.create_jobseeker(**validated_data)
        return user

class AllUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields= '__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_jobseeker(**validated_data)
        return user
    
class UpdateUserSerializer(serializers.Serializer):
    photo = serializers.ImageField(required=False)  # Теперь поле необязательное
    email = serializers.EmailField(read_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance
    

class RegistrateCompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    email = serializers.CharField()
    company_name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only = True)


    def create(self, validated_data):
        user = CustomUser.objects.create_company(**validated_data)
        return user
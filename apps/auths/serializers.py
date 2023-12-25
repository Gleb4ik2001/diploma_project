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
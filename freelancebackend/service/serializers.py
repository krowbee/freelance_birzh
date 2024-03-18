from rest_framework import serializers
from django.contrib.auth.models import User
from executors.serializers import *
from .models import *
class ServiceSerializer(serializers.ModelSerializer):
    #связь с executor serializer
    executor = ExecutorSerializer()
    service_type = serializers.CharField(source='get_service_type_display')

    class Meta:
        model = Service
        fields='__all__'

class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields='__all__'
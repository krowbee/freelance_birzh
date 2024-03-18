from rest_framework import serializers
from django.contrib.auth.models import User
from freelance.serializers import UserSerializer
from .models import *

# Сериализатор executor,
class ExecutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Executor
        fields='__all__'

# Сериализатор создания executor
class CreateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Executor
        fields = '__all__'
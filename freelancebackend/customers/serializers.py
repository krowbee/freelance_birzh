from rest_framework import serializers
from django.contrib.auth.models import User
from freelance.serializers import UserSerializer
from .models import *

#Сериалайзер Кастомерв
class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields='__all__'

# Сериализатор создания Сustomer
class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = '__all__'
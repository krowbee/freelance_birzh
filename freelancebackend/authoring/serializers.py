from rest_framework import serializers
from django.contrib.auth.models import User
from reviews.serializers import ReviewSerializer
from freelance.serializers import UserSerializer
from executors.serializers import ExecutorSerializer
from customers.serializers import CustomerSerializer
from .models import Authoring

class AuthoringSerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    author = UserSerializer()
    executor = ExecutorSerializer()
    customer = CustomerSerializer()

    class Meta:
        model= Authoring
        fields= '__all__'

class CreateAuthoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authoring
        fields='__all__'
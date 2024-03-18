from rest_framework import serializers
from django.contrib.auth.models import User
from executors.serializers import ExecutorSerializer
from customers.serializers import CustomerSerializer
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    customer = CustomerSerializer()

    class Meta:
        model= Message
        fields= '__all__'

class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields='__all__'
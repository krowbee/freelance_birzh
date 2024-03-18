from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ordering
from service.serializers import ServiceSerializer
from order.serializers import OrderSerializer
from executors.serializers import ExecutorSerializer
from customers.serializers import CustomerSerializer

class OrderingSerializer(serializers.ModelSerializer):
    service= ServiceSerializer()
    order = OrderSerializer()
    executor = ExecutorSerializer()
    customer = CustomerSerializer()

    class Meta:
        model= Ordering
        fields= '__all__'

class CreateOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields='__all__'
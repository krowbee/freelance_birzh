from rest_framework import serializers
from django.contrib.auth.models import User
from customers.serializers import *
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    #связь с executor serializer
    customer = CustomerSerializer()
    order_type = serializers.CharField(source='get_order_type_display')

    class Meta:
        model = Order
        fields='__all__'

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'
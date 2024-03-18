from rest_framework import serializers
from django.contrib.auth.models import User
from service.serializers import ServiceSerializer
from order.serializers import OrderSerializer 
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    #связь с executor serializer
    service = ServiceSerializer()
    order = OrderSerializer()

    class Meta:
        model = Tag
        fields='__all__'

class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields='__all__'
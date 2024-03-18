from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields= '__all__'

class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields='__all__'
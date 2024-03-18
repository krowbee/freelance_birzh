from rest_framework import serializers
from django.contrib.auth.models import User
from executors.serializers import ExecutorSerializer
from customers.serializers import CustomerSerializer
from .models import Ticket
class TicketSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    customer = CustomerSerializer()
    severity = serializers.CharField(source='get_severity_display')

    class Meta:
        model= Ticket
        fields= '__all__'

class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields='__all__'
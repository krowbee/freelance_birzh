from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer,CreateCustomerSerializer
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
# Create your views here.

#Функция вывода одного executor'a
class CustomerRetrieveView(RetrieveAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer


#Функция обновления одного executor'a
class CustomerUpdateView(UpdateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CreateCustomerSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class CustomerCreateView(CreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CreateCustomerSerializer

#Функция вывода всех executors
class CustomerListView(ListAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer


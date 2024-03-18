from django.shortcuts import render
from .models import Service
from .serializers import CreateServiceSerializer,ServiceSerializer
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
# Create your views here.

#|||||||||||||||||||||||||||||||||||||||||||||||||||||SERVICE VIEWS|||||||||||||||||||||||||||||


#Функция вывода одного executor'a
class ServiceRetrieveView(RetrieveAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer


#Функция обновления одного executor'a
class ServiceUpdateView(UpdateAPIView):
    queryset=Service.objects.all()
    serializer_class=CreateServiceSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class ServiceCreateView(CreateAPIView):
    queryset=Service.objects.all()
    serializer_class=CreateServiceSerializer


#Функция вывода всех executors
class ServiceListView(ListAPIView):
    #queryset=Service.objects.all()
    serializer_class=ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        params = self.request.query_params
        service_type = params.get('service',None)
        price = params.get('price',None)
        executor = params.get('executor',None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)
        
        if price:
            queryset = queryset.filter(price__lte=price)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        
        return queryset
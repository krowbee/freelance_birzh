from django.shortcuts import render
from .models import Ordering
from .serializers import OrderingSerializer,CreateOrderingSerializer
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
# Create your views here.

#Функция вывода одного executor'a
class OrderingRetrieveView(RetrieveAPIView):
    queryset=Ordering.objects.all()
    serializer_class=OrderingSerializer


#Функция обновления одного executor'a
class OrderingUpdateView(UpdateAPIView):
    queryset=Ordering.objects.all()
    serializer_class=CreateOrderingSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class OrderingCreateView(CreateAPIView):
    queryset=Ordering.objects.all()
    serializer_class=CreateOrderingSerializer


#Функция вывода всех executors
class OrderingListView(ListAPIView):
    queryset=Ordering.objects.all()
    serializer_class=OrderingSerializer
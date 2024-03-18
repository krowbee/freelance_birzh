from django.shortcuts import render
from rest_framework import permissions
from .serializers import ExecutorSerializer,CreateExecutorSerializer
from .models import Executor
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
# Create your views here.

#|||||||||||||||||||||||||||||||||||||||||||||||||||||EXECUTOR VIEWS|||||||||||||||||||||||||||||||||

#Функция вывода одного executor'a
class ExecutorRetrieveView(RetrieveAPIView):
    queryset=Executor.objects.all()
    serializer_class=ExecutorSerializer


#Функция обновления одного executor'a
class ExecutorUpdateView(UpdateAPIView):
    queryset=Executor.objects.all()
    serializer_class=CreateExecutorSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly


#Функция создания нового executor'a
class ExecutorCreateView(CreateAPIView):
    queryset=Executor.objects.all()
    serializer_class=CreateExecutorSerializer


#Функция вывода всех executors
class ExecutorListView(ListAPIView):
    queryset=Executor.objects.all()
    serializer_class=ExecutorSerializer
    

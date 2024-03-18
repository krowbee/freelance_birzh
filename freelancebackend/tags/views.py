from django.shortcuts import render
from .models import Tag
from .serializers import TagSerializer,CreateTagSerializer
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
# Create your views here.

#Функция вывода одного executor'a
class TagRetrieveView(RetrieveAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer


#Функция обновления одного executor'a
class TagUpdateView(UpdateAPIView):
    queryset=Tag.objects.all()
    serializer_class=CreateTagSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class TagCreateView(CreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=CreateTagSerializer

#Функция вывода всех executors
class TagListView(ListAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer
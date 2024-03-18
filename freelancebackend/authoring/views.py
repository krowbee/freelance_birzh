from django.shortcuts import render
from .serializers import AuthoringSerializer,CreateAuthoringSerializer
from .models import Authoring
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
# Create your views here.


#Функция вывода одного executor'a
class AuthoringRetrieveView(RetrieveAPIView):
    queryset=Authoring.objects.all()
    serializer_class=AuthoringSerializer


#Функция обновления одного executor'a
class AuthoringUpdateView(UpdateAPIView):
    queryset=Authoring.objects.all()
    serializer_class=CreateAuthoringSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class AuthoringCreateView(CreateAPIView):
    queryset=Authoring.objects.all()
    serializer_class=CreateAuthoringSerializer
 

#Функция вывода всех executors
class AuthoringListView(ListAPIView):
    queryset=Authoring.objects.all()
    serializer_class=AuthoringSerializer

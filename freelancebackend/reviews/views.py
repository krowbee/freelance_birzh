from django.shortcuts import render
from .serializers import ReviewSerializer,CreateReviewSerializer
from .models import Review
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
# Create your views here.

#|||||||||||||||||||||||||||||||||||||||||||||||||||||EXECUTOR VIEWS|||||||||||||||||||||||||||||||||

#Функция вывода одного executor'a
class ReviewRetrieveView(RetrieveAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer


#Функция обновления одного executor'a
class ReviewUpdateView(UpdateAPIView):
    queryset=Review.objects.all()
    serializer_class=CreateReviewSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class ReviewCreateView(CreateAPIView):
    queryset=Review.objects.all()
    serializer_class=CreateReviewSerializer

#Функция вывода всех executors
class ReviewListView(ListAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

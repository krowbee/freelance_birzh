
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||EXECUTOR URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('reviews/<int:pk>',ReviewRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('reviews/update/<int:pk>',ReviewUpdateView.as_view()),
    #Создание нового executor
    path('reviews/new',ReviewCreateView.as_view()),
    #Вывод всех executors
    path('reviews/all',ReviewListView.as_view()),

]
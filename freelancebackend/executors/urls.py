
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||EXECUTOR URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('executors/<int:pk>',ExecutorRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('executors/update/<int:pk>',ExecutorUpdateView.as_view()),
    #Создание нового executor
    path('executors/new',ExecutorCreateView.as_view()),
    #Вывод всех executors
    path('executors/all',ExecutorListView.as_view()),

]

from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||EXECUTOR URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('message/<int:pk>',MessageRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('message/update/<int:pk>',MessageUpdateView.as_view()),
    #Создание нового executor
    path('message/new',MessageCreateView.as_view()),
    #Вывод всех executors
    path('message/all',MessageListView.as_view()),

]
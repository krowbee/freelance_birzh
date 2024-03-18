
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||TAGS URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('tags/<int:pk>',TagRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('tags/update/<int:pk>',TagUpdateView.as_view()),
    #Создание нового executor
    path('tags/new',TagCreateView.as_view()),
    #Вывод всех executors
    path('tags/all',TagListView.as_view()),

]
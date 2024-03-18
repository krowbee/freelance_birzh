
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||EXECUTOR URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('ordering/<int:pk>',OrderingRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('ordering/update/<int:pk>',OrderingUpdateView.as_view()),
    #Создание нового executor
    path('ordering/new',OrderingCreateView.as_view()),
    #Вывод всех executors
    path('ordering/all',OrderingListView.as_view()),

]
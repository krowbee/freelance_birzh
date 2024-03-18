
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||AUTHORING URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('authoring/<int:pk>',AuthoringRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('authoring/update/<int:pk>',AuthoringUpdateView.as_view()),
    #Создание нового executor
    path('authoring/new',AuthoringCreateView.as_view()),
    #Вывод всех executors
    path('authoring/all',AuthoringListView.as_view()),

]
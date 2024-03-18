
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||SERVICE URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('service/<int:pk>',ServiceRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('service/update/<int:pk>',ServiceUpdateView.as_view()),
    #Создание нового executor
    path('service/new',ServiceCreateView.as_view()),
    #Вывод всех executors
    path('service/all',ServiceListView.as_view()),

]
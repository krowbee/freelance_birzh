
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||EXECUTOR URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('tickets/<int:pk>',TicketRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('tickets/update/<int:pk>',TicketUpdateView.as_view()),
    #Создание нового executor
    path('tickets/new',TicketCreateView.as_view()),
    #Вывод всех executors
    path('tickets/all',TicketListView.as_view()),

]
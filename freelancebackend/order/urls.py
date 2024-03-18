
from django.urls import path
from .views import *



urlpatterns = [
#|||||||||||||||||||||||||||||||ORDER URLS|||||||||||||||||||||||||||||||||||||||||


    #вывод executor по Primary Key
    path('order/<int:pk>',OrderRetrieveView.as_view()),
    #обновление executor по Primary Key
    path('order/update/<int:pk>',OrderUpdateView.as_view()),
    #Создание нового executor
    path('order/new',OrderCreateView.as_view()),
    #Вывод всех executors
    path('order/all',OrderListView.as_view()),

]
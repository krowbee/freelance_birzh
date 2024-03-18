from django.urls import path
from .views import *


urlpatterns = [
#|||||||||||||||||||||||||||||||CUSTOMER URLS|||||||||||||||||||||||||||||||||||||||||
    
     #вывод Customer по Primary Key
    path('customers/<int:pk>',CustomerRetrieveView.as_view()),
    #обновление Customer по Primary Key
    path('customers/update/<int:pk>',CustomerUpdateView.as_view()),
    #Создание нового Customer
    path('customers/new',CustomerCreateView.as_view()),
    #Вывод всех customers
    path('customers/all',CustomerListView.as_view()),

]
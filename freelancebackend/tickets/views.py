from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
from .models import Ticket
from .serializers import TicketSerializer,CreateTicketSerializer
# Create your views here.
#Функция вывода одного executor'a
class TicketRetrieveView(RetrieveAPIView):
    queryset=Ticket.objects.all()
    serializer_class=TicketSerializer


#Функция обновления одного executor'a
class TicketUpdateView(UpdateAPIView):
    queryset=Ticket.objects.all()
    serializer_class=CreateTicketSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class TicketCreateView(CreateAPIView):
    queryset=Ticket.objects.all()
    serializer_class=CreateTicketSerializer

#функция вывода всех тикетов
class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
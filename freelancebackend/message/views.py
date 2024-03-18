from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer,CreateMessageSerializer
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions
# Create your views here.

#Функция вывода одного executor'a
class MessageRetrieveView(RetrieveAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer


#Функция обновления одного executor'a
class MessageUpdateView(UpdateAPIView):
    queryset=Message.objects.all()
    serializer_class=CreateMessageSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class MessageCreateView(CreateAPIView):
    queryset=Message.objects.all()
    serializer_class=CreateMessageSerializer


#Функция вывода всех executors
class MessageListView(ListAPIView):
    #queryset=Message.objects.all()
    serializer_class=MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()
        params = self.request.query_params
        executor = params.get('executor',None)
        customer = params.get('customer',None)
        from_date= params.get('from_date',None)
        to_date = params.get('to_date',None)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        if customer:
            queryset = queryset.filter(customer__id=customer)
        
        if from_date:
            queryset = queryset.filter(msg_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(msg_date__lte=to_date)

        
        return queryset
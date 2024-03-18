from django.shortcuts import render
from .models import Order
from .serializers import CreateOrderSerializer
from .serializers import OrderSerializer
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,ListAPIView
from rest_framework import permissions

# Create your views here.

#|||||||||||||||||||||||||||||||||ORDER VIEWS|||||||||||||||||||||||||||||\
    
#Функция вывода одного executor'a
class OrderRetrieveView(RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


#Функция обновления одного executor'a
class OrderUpdateView(UpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=CreateOrderSerializer
    permission_class=permissions.IsAuthenticatedOrReadOnly

#Функция создания нового executor'a
class OrderCreateView(CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=CreateOrderSerializer

#Функция вывода всех executors
class OrderListView(ListAPIView):
    #queryset=Order.objects.all()
    serializer_class=OrderSerializer


    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params
        order_type = params.get('order',None)
        price = params.get('price',None)
        customer = params.get('customer',None)

        if order_type:
            queryset = queryset.filter(order_type=order_type)
        
        if price:
            queryset = queryset.filter(price__lte=price)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        
        return queryset
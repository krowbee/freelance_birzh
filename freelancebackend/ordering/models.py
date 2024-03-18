from django.db import models
from customers.models import Customer
from executors.models import Executor
from service.models import Service
from order.models import Order
# Create your models here.

class Ordering(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor,on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    deadline  = models.DateTimeField()

    def __str__(self):
        return self.customer, self.executor, self.order
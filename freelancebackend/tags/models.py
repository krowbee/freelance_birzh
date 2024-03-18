from django.db import models
from service.models import Service
from order.models import Order
# Create your models here.

class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
    
    name = models.CharField(max_length=128)
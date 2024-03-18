from django.db import models
from customers.models import Customer
from executors.models import Executor
# Create your models here.

class Message(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor,on_delete=models.CASCADE)
    msg_date= models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField()
    desc = models.TextField()
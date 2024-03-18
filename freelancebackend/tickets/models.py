from django.db import models
from customers.models import Customer
from executors.models import Executor
# Create your models here.

class Ticket(models.Model):
    SEVERITIES = [
        ('low',' Low'),
        ('med','Medium'),
        ('high','High'),
    ]

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    executor = models.ForeignKey(Executor,on_delete=models.CASCADE,blank=True,null=True)
    datetime= models.DateTimeField(auto_now_add=True)
    severity = models.CharField(choices=SEVERITIES,default='low',max_length=10)
    desc = models.TextField(("Описание") )
    is_resolved = models.BooleanField(default=False)
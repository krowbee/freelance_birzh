from django.db import models
from customers.models import Customer
# Create your models here.

class Order(models.Model):
    SERVICE_TYPES = [
        ('web','Web Development'),
        ('markt','Marketing'),
        ("copy","Copywriting"),
        ('rwrite','Rewriting'),
        ("trans","Translating"),
        ('video','Video-Making'),
        ('photo',"Photoshop")
    ]
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=128)
    desc = models.TextField('Описание')
    price = models.IntegerField("Цена")
    order_type = models.CharField(choices=SERVICE_TYPES,max_length=12,default='web')

    def __str__(self):
        return self.name,  self.get_order_type_display(), self.price
from django.db import models
from executors.models import *
# Create your models here.

class Service(models.Model):
    SERVICE_TYPES = [
        ('web','Web Development'),
        ('markt','Marketing'),
        ("copy","Copywriting"),
        ('rwrite','Rewriting'),
        ("trans","Translating"),
        ('video','Video-Making'),
        ('photo',"Photoshop"),
    ]
    executor = models.ForeignKey(Executor,on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=128)
    desc = models.TextField('Описание')
    price = models.IntegerField("Цена")
    service_type = models.CharField(choices=SERVICE_TYPES,max_length=12,default='web')

    def __str__(self):
        return self.name
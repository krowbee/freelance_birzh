from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Executor(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField('Номер телефона:', max_length=128)
    
    def __str__(self):
        return self.user.username

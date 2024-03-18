from django.db import models
from reviews.models import Review
from django.contrib.auth.models import User
from customers.models import Customer
from executors.models import Executor
# Create your models here.

class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    executor = models.ForeignKey(Executor,on_delete=models.CASCADE,blank=True,null=True)
    review_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author, self.review_date
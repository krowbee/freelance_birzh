from django.db import models

# Create your models here.

class Review(models.Model):
    RATING_FILLED=[
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('5',5)
    ]

    rating = models.CharField(choices=RATING_FILLED,default='1',max_length=1)
    desc= models.CharField(max_length=1000)
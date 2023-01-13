from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    price = models.FloatField()
    stock = models.BooleanField(default=True)

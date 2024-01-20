from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=10)

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
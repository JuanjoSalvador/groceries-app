from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self, *args, **kwargs):
        return f"{self.name}"

class Price(models.Model):
    date = models.DateField()
    value = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self, *args, **kwargs):
        return f"{self.value}€/unidad en {self.store.name}"

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self, *args, **kwargs):
        return f"{self.name}"
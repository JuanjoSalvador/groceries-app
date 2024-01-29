from datetime import date

from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self, *args, **kwargs):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80, default="")
    description = models.CharField(max_length=500, default="")
    price = models.FloatField()
    weight = models.FloatField(blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)

    def __str__(self, *args, **kwargs):
        return f"{self.name} - {self.brand}"
    
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        ProductHistory.objects.create(
            product = self,
            price = self.price,
            date = date.today()
        )

class ProductHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = price = models.FloatField()
    date = models.DateField()

    def __str__(self, *args, **kwargs):
        return f"{self.product.name} - {self.product.brand} ({self.date})"

    class Meta:
        verbose_name = "Price history"
        verbose_name_plural = "Price history"

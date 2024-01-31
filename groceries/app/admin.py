from django.contrib import admin
from .models import Product, ProductHistory, Store

admin.site.register(Product)
admin.site.register(Store)

admin.site.register(ProductHistory)

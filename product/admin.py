from django.contrib import admin
from .models import Product ,voted_product

# Register your models here.

admin.site.register(Product)
admin.site.register(voted_product)
from django.contrib import admin
from products.models import AllProducts, SoldProducts

# Register your models here.
admin.site.register(AllProducts)
admin.site.register(SoldProducts)
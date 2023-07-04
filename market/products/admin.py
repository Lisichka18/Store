from django.contrib import admin

from products.models import ProductsCategory, Products

admin.site.register(ProductsCategory)
admin.site.register(Products)

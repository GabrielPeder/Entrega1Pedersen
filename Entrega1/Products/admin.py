from django.contrib import admin
from Products.models import Product


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price', 'stock')
    list_filter = ('stock',)
    search_fields = ('name', )
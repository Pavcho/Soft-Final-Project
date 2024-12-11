from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available')
    search_fields = ('name',)
    list_filter = ('available',)

admin.site.register(Product, ProductAdmin)


from django.contrib import admin
from .models import CustomUser, ShippingAddress, Funds, Cart

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active',)
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')

admin.site.register(CustomUser, CustomUserAdmin)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('address_line_1', 'address_line_2', 'country', 'city', 'zipcode')
    search_fields = ('address_line_1', 'address_line_2', 'country')
    list_filter = ('country','city', 'zipcode')

admin.site.register(ShippingAddress, ShippingAddressAdmin)


class FundsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sum', 'last_buy', 'last_deposit')
    search_fields = ('id',)
    list_filter = ('sum',)

admin.site.register(Funds, FundsAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
    list_filter = ('id',)

admin.site.register(Cart, CartAdmin)

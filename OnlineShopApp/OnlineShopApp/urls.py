"""
URL configuration for OnlineShopApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from OnlineShopApp import views
from OnlineShopApp.views import CartPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('contact-us',views.ContactUsView.as_view(), name='contact_us'),
    path('accounts/', include('accountsUsersApp.urls')),
    path('products/', include('ProductsApp.urls')),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('buy-from-cart/<str:whole_price>/', views.buy_from_cart, name='buy_from_cart'),
    path('remove-all-from-cart/', views.remove_all_from_card,name='remove_all_from_cart'),
    path('edit_products_button/<int:product_id>', views.edit_products_button, name='edit_products_button'),
    path('delete_products_button/<int:product_id>', views.delete_products_button, name='delete_products_button'),
    path('successful-payment/', views.SuccessfulPaymentView.as_view(), name='successful_payment'),
    path('successful-deposit/', views.SuccessfulDepositView.as_view(), name='successful_deposit'),
    path('cart/',CartPageView.as_view(), name='cart'),
]
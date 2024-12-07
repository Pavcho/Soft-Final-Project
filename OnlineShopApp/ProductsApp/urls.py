from django.urls import path
from ProductsApp.views import ProductsPageView

urlpatterns = [
    path('', ProductsPageView.as_view(), name='products_page'),
]
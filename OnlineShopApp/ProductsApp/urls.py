from django.urls import path
from ProductsApp.views import ProductsPageView, ManageProductsPageView, ProductsUpdateView

urlpatterns = [
    path('', ProductsPageView.as_view(), name='products_page'),
    path('manage/', ManageProductsPageView.as_view(), name='manage_products_page'),
    path('updateProduct/<int:pk>', ProductsUpdateView.as_view(), name='update_product'),
]
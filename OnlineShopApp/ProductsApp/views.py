from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from ProductsApp.forms import ProductEditForm
from ProductsApp.models import Product


class ProductsPageView(TemplateView):
    template_name = "products/product_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
            context['funds'] = user.funds.sum
            context['cart_list'] = user.cart.item_ids
            context['is_staff_user'] = user.groups.filter(name="Users_Staff").exists()
        context['products'] = Product.objects.all()
        return context


class ManageProductsPageView(UserPassesTestMixin, TemplateView):
    template_name = "products/manage_products.html"

    def test_func(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='Users_Staff').exists():
            return True

    def handle_no_permission(self):
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
            context['funds'] = user.funds.sum
            context['cart_list'] = user.cart.item_ids
        context['products'] = Product.objects.all()
        return context


class ProductsUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    pk_url_kwarg = 'pk'
    template_name = 'products/update_products_view.html'
    success_url = reverse_lazy('manage_products_page')

    def test_func(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='Users_Staff').exists():
            return True

    def handle_no_permission(self):
        return redirect('home')

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
            context['funds'] = user.funds.sum
        return context
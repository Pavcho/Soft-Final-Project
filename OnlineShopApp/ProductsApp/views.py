from django.views.generic import TemplateView

from ProductsApp.models import Product


class ProductsPageView(TemplateView):
    template_name = "products/product_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
        context['products'] = Product.objects.all()
        return context

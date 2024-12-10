from decimal import Decimal

from django.shortcuts import redirect
from django.views.generic import TemplateView
from accountsUsersApp.models import Cart
from ProductsApp.models import Product


class IndexView(TemplateView):
    template_name = "main_templates/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
            context['funds'] = user.funds.sum
        return context

class ContactUsView(TemplateView):
    template_name = "main_templates/contact_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
            context['funds'] = user.funds.sum
        return context

class SuccessfulPaymentView(TemplateView):
    template_name = "products/successful_payment.html"

class SuccessfulDepositView(TemplateView):
    template_name = "products/successful_deposit.html"

# a view when the add to cart button is clicked
def add_to_cart(request, product_id):
    user = request.user

    if not user.cart:
        user.cart = Cart.objects.create()
        user.save()

    if product_id not in user.cart.item_ids:
        user.cart.item_ids.append(product_id)
        user.cart.save()
        return redirect('products_page')

    return redirect('products_page')

def buy_from_cart(request, whole_price):
    user = request.user
    whole_price = float(whole_price)

    if user.funds.sum >= whole_price:
        if user.shipping_address.address_line_1:
            user.funds.sum -= Decimal(str(whole_price))
            user.funds.last_buy = float(whole_price)
            user.funds.save()
            user.cart.item_ids = []
            user.cart.save()
            return redirect('successful_payment')
        else:
            print("Invalid address! Please put in your address.")
            return redirect('profile_change_address')
    else:
        print("You don't have enough funds!")
        return redirect('profile_deposit')

    return redirect('products_page')

def remove_all_from_card(request):
    user = request.user
    user.cart.item_ids = []
    user.cart.save()
    return redirect('cart')

class CartPageView(TemplateView):
    template_name = "products/cart_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        if user.is_authenticated:
            context['username'] = user.username
            products_array = []
            whole_price = 0
            for product in Product.objects.all():
                if product.id in user.cart.item_ids:
                    products_array.append(product)
                    whole_price += product.price
            context['products'] = products_array
            context['whole_price_display'] = f"{whole_price:,.2f}"
            context['whole_price'] = whole_price
            context['funds'] = user.funds.sum
        return context
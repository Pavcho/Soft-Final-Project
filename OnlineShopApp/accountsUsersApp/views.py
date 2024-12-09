from datetime import date

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountsUsersApp.forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserEditForm, \
    ShippingAddressEditForm, FundsDepositForm
from accountsUsersApp.models import CustomUser, ShippingAddress, Funds, Cart


# a view for register
class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.instance
        user.shipping_address = ShippingAddress.objects.create()
        user.funds = Funds.objects.create()
        user.cart = Cart.objects.create()
        user.save()

        return response


# a view for login
class UserLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')


# a view for logout
def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')


# a view for checking profile details
class UserProfileView(DetailView, LoginRequiredMixin):
    model = CustomUser
    pk_url_kwarg = 'pk'
    template_name = 'accounts/view_profile_details.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        shipping_address = user.shipping_address
        funds = user.funds
        context['shipping_address'] = shipping_address
        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['email'] = user.email
        context['phone'] = user.phone
        if funds:
            context['funds'] = funds.sum
        if shipping_address:
            context['address_line_1'] = shipping_address.address_line_1
            context['address_line_2'] = shipping_address.address_line_2
            context['city'] = shipping_address.city
            context['country'] = shipping_address.country
            context['zipcode'] = shipping_address.zipcode
        return context


# a view for editing profile details
class UserEditProfileView(UpdateView, LoginRequiredMixin):
    model = CustomUser
    form_class = CustomUserEditForm
    pk_url_kwarg = 'pk'
    template_name = 'accounts/edit_profile_details.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username
        return context


# a view for deleting the profile
class UserDeleteProfileView(DeleteView, LoginRequiredMixin):
    model = CustomUser
    pk_url_kwarg = 'pk'
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = self.request.user

        if user.shipping_address:
            user.shipping_address.delete()

        if user.funds:
            user.funds.delete()

        if user.cart:
            user.cart.delete()

        logout(self.request)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username
        return context


# a view for selecting an address
class UserEditAddressView(UpdateView, LoginRequiredMixin):
    model = ShippingAddress
    form_class = ShippingAddressEditForm
    pk_url_kwarg = 'pk'
    template_name = 'accounts/select_profile_address.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        user = self.request.user
        if not user.shipping_address:
            user.shipping_address = ShippingAddress.objects.create()
            user.save()
        return user.shipping_address

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username
        return context


# a view for depositing funds
class UserDepositFundsView(UpdateView, LoginRequiredMixin):
    model = Funds
    form_class = FundsDepositForm
    pk_url_kwarg = 'pk'
    template_name = 'accounts/deposit_funds_profile.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        user = self.request.user
        if not user.funds:
            user.funds = Funds.objects.create()
            user.save()
        return user.funds

    def form_valid(self, form):
        user = self.request.user
        current_user_funds = user.funds
        current_user_funds.sum += current_user_funds.last_deposit
        current_user_funds.temporary_placeholder_name = ""
        current_user_funds.temporary_CVV = ""
        current_user_funds.temporary_card_number = ""
        current_user_funds.expiration_date = date.today()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username
        return context


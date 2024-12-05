from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountsUsersApp.forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserEditForm
from accountsUsersApp.models import CustomUser


# a view for register
class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')


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
        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['email'] = user.email
        context['phone'] = user.phone
        context['preferred_address'] = user.preferred_address
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username
        return context

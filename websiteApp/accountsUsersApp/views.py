from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accountsUsersApp.forms import CustomUserCreationForm, CustomUserLoginForm


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
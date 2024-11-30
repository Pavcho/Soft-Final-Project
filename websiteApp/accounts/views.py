from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm, CustomUserLoginForm


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')


class UserLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')


def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')
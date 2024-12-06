from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from accountsUsersApp.models import ShippingAddress


# form for registering a user, it will require username, email, phone and address
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email','phone')


# form for login, it will require username and password
class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')


class ShippingAddressEditForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
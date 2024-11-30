from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# form for registering a user, it will require username, email, phone and address
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'email','phone', 'preferred_address')


# form for login, it will require username and password
class CustomUserLoginForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = get_user_model()
        fields = ('email', 'password')
from django.urls import path
from accountsUsersApp.views import UserRegisterView, UserLoginView, logout_view, UserProfileView, UserEditProfileView, \
    UserDeleteProfileView, UserEditAddressView, UserDepositFundsView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('view/', UserProfileView.as_view(), name='profile_details'),
    path('edit/', UserEditProfileView.as_view(), name='profile_edit'),
    path('delete/', UserDeleteProfileView.as_view(), name='profile_delete'),
    path('change_address/', UserEditAddressView.as_view(), name='profile_change_address'),
    path('deposit/', UserDepositFundsView.as_view(), name='profile_deposit'),
]
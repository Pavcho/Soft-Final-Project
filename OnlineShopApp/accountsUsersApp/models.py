from django.contrib.auth.models import AbstractUser
from django.db import models

from accountsUsersApp.validators import AllNumbersValidator, TenCharactersValidator


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10,
                                unique=True,)

    phone = models.CharField(unique=True,
                             validators=[
                                 AllNumbersValidator(),
                                 TenCharactersValidator(),
                             ])

    shipping_address = models.ForeignKey(to='ShippingAddress',
                                         on_delete=models.CASCADE,
                                         related_name='shipping_address',
                                         null=True,
                                         blank=True)

class ShippingAddress(models.Model):
   address_line_1 = models.CharField(
       max_length=100,
       help_text="Address Line 1",
   )

   address_line_2 = models.CharField(
       max_length=100,
       blank=True,
       null=True,
       help_text="Address Line 2",
   )

   city = models.CharField(
       max_length=20,
       help_text="City",
   )

   country = models.CharField(
       max_length=20,
       help_text="Country",
   )

   zipcode = models.CharField(
       max_length=10,
       help_text="Zip Code",
   )


# class Cart(models.Model):
#     pass
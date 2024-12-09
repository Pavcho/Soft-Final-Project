from datetime import date
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.core.validators import DecimalValidator, MinValueValidator, MinLengthValidator
from django.db import models
from accountsUsersApp.validators import AllNumbersValidator, TenCharactersValidator


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10,
                                unique=True)

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

    funds = models.ForeignKey(to='Funds',
                              on_delete=models.CASCADE,
                              related_name='funds',
                              null=True,
                              blank=True)

    cart = models.ForeignKey(to='Cart',
                             on_delete=models.CASCADE,
                             related_name='cart',
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

class Funds(models.Model):
    sum = models.DecimalField(default=0.0,
                              max_digits=6,
                              decimal_places=2,)

    last_deposit = models.DecimalField(default=0.0,
                                       max_digits=6,
                                       decimal_places=2,
                                       validators=[
                                           DecimalValidator(max_digits=6, decimal_places=2),
                                           MinValueValidator(0.01)],
                                       help_text="Deposit here",
                                       )

    last_buy = models.DecimalField(default=0.0,
                                   max_digits=6,
                                   decimal_places=2)

    temporary_placeholder_name = models.CharField(default="",
                                                  max_length=30,)

    temporary_card_number = models.CharField(default="",
                                             max_length=16,
                                             validators=[
                                                 TenCharactersValidator(),
                                                 AllNumbersValidator()
                                             ])

    temporary_expiration_date = models.DateField(default=date.today())

    temporary_CVV = models.CharField(default="",
                                     validators=[
                                         AllNumbersValidator(),
                                         MinLengthValidator(3),
                                     ],
                                     max_length=3,
                                     verbose_name="CVV",)

class Cart(models.Model):
    item_ids = ArrayField(models.IntegerField(), blank=True, default=list)
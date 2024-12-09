# Generated by Django 5.1.3 on 2024-12-08 20:07

import accountsUsersApp.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0011_alter_funds_last_deposit_alter_funds_sum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds',
            name='last_buy',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='funds',
            name='temporary_CVV',
            field=models.CharField(default='', max_length=3, validators=[accountsUsersApp.validators.AllNumbersValidator(), django.core.validators.MinValueValidator(3)], verbose_name='CVV'),
        ),
    ]
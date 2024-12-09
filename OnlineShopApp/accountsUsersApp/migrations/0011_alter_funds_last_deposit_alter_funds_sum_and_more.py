# Generated by Django 5.1.3 on 2024-12-08 20:01

import accountsUsersApp.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0010_alter_funds_temporary_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds',
            name='last_deposit',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Deposit here', max_digits=4, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=4), django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='funds',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='funds',
            name='temporary_CVV',
            field=models.CharField(default='', help_text='CVV', max_length=3, validators=[accountsUsersApp.validators.AllNumbersValidator()]),
        ),
    ]
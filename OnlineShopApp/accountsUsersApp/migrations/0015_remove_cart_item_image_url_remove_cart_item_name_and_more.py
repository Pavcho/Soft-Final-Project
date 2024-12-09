# Generated by Django 5.1.3 on 2024-12-09 13:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0014_cart_alter_funds_temporary_expiration_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item_image_url',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item_price',
        ),
        migrations.AddField(
            model_name='cart',
            name='item_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-09 14:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0015_remove_cart_item_image_url_remove_cart_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=None),
        ),
    ]

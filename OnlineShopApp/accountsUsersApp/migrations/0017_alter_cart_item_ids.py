# Generated by Django 5.1.3 on 2024-12-09 14:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0016_alter_cart_item_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
    ]

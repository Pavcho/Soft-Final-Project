# Generated by Django 5.1.3 on 2024-12-10 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0018_alter_funds_temporary_card_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds',
            name='temporary_expiration_date',
            field=models.DateField(default=datetime.date(2024, 12, 10)),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-15 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0021_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text={'max_length': "The user's username must be 10 characters or less.", 'unique': 'A user with that username already exists.'}, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='funds',
            name='temporary_expiration_date',
            field=models.DateField(default=datetime.date(2024, 12, 15)),
        ),
    ]
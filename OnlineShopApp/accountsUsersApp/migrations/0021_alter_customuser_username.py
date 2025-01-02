# Generated by Django 5.1.3 on 2024-12-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsUsersApp', '0020_alter_funds_temporary_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'max_length': "The user's username must be 10 characters or less.", 'unique': 'A user with that username already exists.'}, max_length=10, unique=True),
        ),
    ]
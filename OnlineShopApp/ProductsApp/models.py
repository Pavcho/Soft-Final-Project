from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20,
                            unique=True,
                            error_messages={'Name should be unique': 'A product with this name already exists.'},
                            help_text="Name")

    price = models.FloatField(help_text="Price")

    available = models.BooleanField(default=True,
                                    help_text="Is this product available?")

    image_url = models.URLField(help_text="Image URL")

from django.core.exceptions import ValidationError
from django.db import DataError, IntegrityError
from django.test import TestCase
from .models import Product

class ProductsTestCase(TestCase):

    def test_product_creation(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=100,
            available=True,
            image_url="https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg"
        )

        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.available, True)
        self.assertEqual(self.product.image_url, "https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg")


    def test_product_creation_with_too_long_name(self):
        def create_product_with_too_long_name():
            self.product = Product.objects.create(
                name="Test Product Test Product",
                price=100,
                available=True,
                image_url="https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg"
            )

        self.assertRaises(DataError, create_product_with_too_long_name)


    def test_product_creation_with_no_name(self):
        self.product = Product.objects.create(
            name="",
            price=100,
            available=True,
            image_url="https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg"
        )

        self.assertRaises(ValidationError, self.product.full_clean)


    def test_product_creation_with_already_taken_name(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=100,
            available=True,
            image_url="https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg")

        def create_product_with_already_taken_name():
            self.product2 = Product.objects.create(
                name="Test Product",
                price=120,
                available=False,
                image_url="https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg")

        self.assertRaises(IntegrityError, create_product_with_already_taken_name)


    def test_product_creation_with_default_availability(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=100,
            image_url="https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg"
        )

        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.available, True)
        self.assertEqual(self.product.image_url, "https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg")


    def test_product_creation_with_negative_price(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=-100,
            available=True,
            image_url="https://m.media-amazon.com/images/I/41dIwrJSJHS.jpg")

        self.assertRaises(ValidationError, self.product.full_clean)
from django.core.exceptions import ValidationError
from django.db import DataError, IntegrityError
from django.test import TestCase
from accountsUsersApp.models import CustomUser, ShippingAddress, Funds, Cart


class CustomUserTest(TestCase):

    def test_user_creation(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="1111111111",
            email="a@abv.bg",
            password="123test123"
        )

        self.assertEqual(self.user.username, "Test1")
        self.assertEqual(self.user.phone, "1111111111")
        self.assertEqual(self.user.email, "a@abv.bg")


    def test_user_creation_with_no_username(self):
        def create_nameless_user():
            self.user = CustomUser.objects.create_user(
            username="",
            phone="2222222222",
            email="b@abv.bg",
            password="123paco123"
        )

        self.assertRaises(ValueError, create_nameless_user)


    def test_user_creation_with_too_long_username(self):
        def create_user_with_too_long_username():
            self.user = CustomUser.objects.create_user(
            username="TestLongUsername",
            phone="3333333333",
            email="c@abv.bg",
            password="123paco123"
        )

        self.assertRaises(DataError, create_user_with_too_long_username)


    def test_user_creation_with_already_taken_username(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="1111111111",
            email="a@abv.bg",
            password="123test123"
        )

        def create_user_with_already_taken_username():
            self.second_user = CustomUser.objects.create_user(
                username="Test1",
                phone="2222222222",
                email="b@abv.bg",
                password="123test123"
            )

        self.assertRaises(IntegrityError, create_user_with_already_taken_username)


    def test_user_creation_with_invalid_email(self):
        self.user = CustomUser.objects.create_user(
            username="Test5",
            phone="5555555555",
            email="e_invalid_email",
            password="123paco123"
        )

        self.assertRaises(ValidationError, self.user.full_clean)


    def test_user_creation_with_already_taken_phone(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="1111111111",
            email="a@abv.bg",
            password="123test123"
        )

        def create_user_with_already_taken_phone():
            self.user2 = CustomUser.objects.create_user(
                username="Test1",
                phone="1111111111",
                email="a@abv.bg",
                password="123test123"
            )

        self.assertRaises(IntegrityError, create_user_with_already_taken_phone)


    def test_user_creation_with_letters_in_phone_number(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="a111111111",
            email="a@abv.bg",
            password="123test123"
        )

        self.assertRaises(ValidationError, self.user.full_clean)


    def test_user_creation_with_too_long_phone_number(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="11111111112222222222",
            email="a@abv.bg",
            password="123test123"
        )

        self.assertRaises(ValidationError, self.user.full_clean)


    def test_user_creation_with_too_short_phone_number(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="111",
            email="a@abv.bg",
            password="123test123"
        )

        self.assertRaises(ValidationError, self.user.full_clean)


    def test_shipping_address_with_values_added_to_user(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="1111111111",
            email="a@abv.bg",
            password="123test123"
        )

        self.user.shipping_address = ShippingAddress.objects.create(
            address_line_1="1",
            address_line_2="2",
            city="3",
            country="4",
            zipcode="5",
        )

        self.assertEqual(self.user.shipping_address_id, 1)
        self.assertEqual(self.user.shipping_address.address_line_1, "1")
        self.assertEqual(self.user.shipping_address.address_line_2, "2")
        self.assertEqual(self.user.shipping_address.city, "3")
        self.assertEqual(self.user.shipping_address.country, "4")
        self.assertEqual(self.user.shipping_address.zipcode, "5")


    def test_funds_added_to_user(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="1111111111",
            email="a@abv.bg",
            password="123test123"
        )
        self.user.funds = Funds.objects.create()

        self.assertEqual(self.user.funds_id, 1)


    def test_cart_added_to_user(self):
        self.user = CustomUser.objects.create_user(
            username="Test1",
            phone="1111111111",
            email="a@abv.bg",
            password="123test123"
        )
        self.user.cart = Cart.objects.create()

        self.assertEqual(self.user.cart_id, 1)
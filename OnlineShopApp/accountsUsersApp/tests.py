from django.core.exceptions import ValidationError
from django.db import DataError, IntegrityError
from django.test import TestCase
from accountsUsersApp.models import CustomUser


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
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):

    def test_create_user_with_email(self):
        email = "akash@gmail.co"
        password = 'cft6cft6'
        user = get_user_model().objects.create_user(
            email=email,
            password=password

        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_enail_normalized(self):
        """Test the email for a new user"""
        email = 'test@GMAIL.COM'
        user =  get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email,email.lower())

    def test_new_user_with_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"test123")


    def test_create_superuser(self):
        """Test creating new superuser"""

        user = get_user_model().objects.create_superuser(
            'admin@admin.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
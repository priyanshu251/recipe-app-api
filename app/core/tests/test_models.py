from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "user@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(         
            email=email,
            password=password
        )
        # get_user_model()--a function in django used to retrieve user model currently active in this project. If there is no custom user model defined, it will return the default user model provided by Django(django.contrib.auth.models.User)
        self.assertEqual(user.email, email)   # user here is the object of the user model
        self.assertTrue(user.check_password(password))  # we are using check_password method to check the password because the password is hashed and stored in the database. The check_password method provided by Django hashes the input password and compares it with the stored password hash to verify the password.

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_emails=[
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['TEST3@example.COM', 'TEST3@example.com'],
            ['Test4@example.Com', 'Test4@example.com']
        ]
        for email, expected in sample_emails:
            user=get_user_model().objects.create_user(email, 'test123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """"Test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test123')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@example.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff) 
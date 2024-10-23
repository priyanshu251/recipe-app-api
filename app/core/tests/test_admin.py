"""Test for django admin modifications"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse #A function that returns the URL path for a given view name. It is useful for generating URLs dynamically.

class AdminSiteTests(TestCase):

    #This setUp method is called before each test method to set up any state that is shared among the tests. It is useful for creating objects that are used in multiple tests.
    def setUp(self):
        """create user and client"""
        self.client = Client()  # An instance of the Client class, a class that acts as a dummy web browser, allowing you to simulate GET and POST requests on a URL and observe the response.

        # instance of admin_user
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='test123',
        )
        self.client.force_login(self.admin_user) #Logs in the admin user without requiring a password. This is useful for testing purposes. This is particularly useful in tests to bypass the login process and directly test the functionality that requires an authenticated user.

        # instance of regular user
        self.user=get_user_model().objects.create_user(
            email='user@exmaple.com',
            password='test123',
            name='Test user'
        )


    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')  #generate the URL for the user change list page in the admin interface.
        res=self.client.get(url)

        self.assertContains(res, self.user.name)   
        self.assertContains(res, self.user.email)


# NOTE: admin user is created just to access the django admin page which will show the list of all users(regular). Hence first a admin user is setup and then regular user is created in test database. URL is extracted using reverse function and GET req is made. response conatins all teh list of regular user. 

# This test wont work until we write the code for custom admin
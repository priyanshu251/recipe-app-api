from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    # function name should be consistent with the Django convention
    def create_user(self, email, password=None, **extra_fields): # **extra_fields is used to accept any number of additional keyword arguments. It can be name or any other field that we want to add to the user model. This function will automatically create a user model with the provided email and password.
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields) # self.model is used to create a new model instance. It is used to create a new user model instance with the provided email and any additional fields. In this case it wil be be object of class User that we defined.
        user.set_password(password)  # set_password method provided by Django hashes the password before saving it to the database.
        user.save(using=self._db)  # self._db is used to support multiple databases. It is used to save the user model instance to the database.
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser with given email and password"""
        user = self.create_user(email, password)    # first create a user self defined create_user method
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # objects is a default attribute of Django models that is used to manage the model instances. We are overriding the default objects attribute with our custom UserManager class.

    USERNAME_FIELD = 'email'

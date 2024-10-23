from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

class UserAdmin(BaseUserAdmin):  # ye baseuseradmin uppar wala useradmin hai jo alias kiya gya hai
    """define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']  

admin.site.register(models.User, UserAdmin)

# This code is configuring the Django admin interface to manage a custom user model. The Django admin interface is a built-in feature that provides a web-based interface for managing the data in your application. By default, Django includes a user model and an admin interface for managing users, but this code customizes that interface to work with a custom user model.
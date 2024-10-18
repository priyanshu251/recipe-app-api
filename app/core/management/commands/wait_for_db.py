"""command for django app to wait for db to get ready"""

from django.core.management.base import BaseCommand
# This line imports the BaseCommand class from Django's core.management.base module. BaseCommand is a base class for creating custom management commands in Django. By inheriting from BaseCommand, you can define your own commands that can be run using Django's manage.py script.

class Command(BaseCommand):
    # This line defines a new class named Command that inherits from BaseCommand. The name Command is significant because Django looks for a class with this name when it searches for custom management commands. By inheriting from BaseCommand, the Command class gains the ability to be executed as a management command.
    
    def handle(self, *args, **options): # This line defines a handle() method on the Command class. This method is called when the management command is executed. The handle() method takes two arguments: *args and **options. The *args argument is a list of positional arguments, and the **options argument is a dictionary of keyword arguments.
        pass
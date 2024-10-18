"""command for django app to wait for db to get ready"""

import time
from django.core.management.base import BaseCommand
# This line imports the BaseCommand class from Django's core.management.base module. BaseCommand is a base class for creating custom management commands in Django. By inheriting from BaseCommand, you can define your own commands that can be run using Django's manage.py script.
from psycopg2 import OperationalError as Psycopg2OpError  # this op error is raised by postgresql when db is not ready as psycopg2 is the db adapter for postgresql
from django.db.utils import OperationalError  # this op error is raised by django when db is not ready
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # This line defines a new class named Command that inherits from BaseCommand. The name Command is significant because Django looks for a class with this name when it searches for custom management commands. By inheriting from BaseCommand, the Command class gains the ability to be executed as a management command.
    
    def handle(self, *args, **options): # This line defines a handle() method on the Command class. This method is called when the management command is executed. The handle() method takes two arguments: *args and **options. The *args argument is a list of positional arguments, and the **options argument is a dictionary of keyword arguments.
        self.stdout.write('Waiting for database...')    
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))    
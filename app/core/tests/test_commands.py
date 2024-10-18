""" test for custom django management command """

from unittest.mock import patch # This line imports the patch function from the unittest.mock module. The patch function is used to temporarily replace the target object with a mock object during the test.

from psycopg2 import OperationalError as psycopg2Error # This line imports the OperationalError exception from the psycopg2 module and renames it to psycopg2Error. This exception is used to handle database-related errors specific to PostgreSQL.

from django.core.management import call_command # This line imports the call_command function from django.core.management. The call_command function is used to programmatically call a Django management command.

from django.db.utils import OperationalError  # This line imports the OperationalError exception from django.db.utils. This exception is used to handle general database-related errors
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')  # This line uses the patch decorator to mock the check method of the Command class in the wait_for_db module (check method is not explicitly defined in the Command class but the Command class inherits BaseCommand there exists the check method- This method is used to perform system checks, including database checks, to ensure that everything is configured correctly). The patch decorator replaces the check method with a mock object for the duration of the test.
class CommandTests(SimpleTestCase):

    # this function is used to test the wait_for_db command assuming the database is ready
    def test_wait_for_db_ready(self,patched_check):  # The patched_check parameter is the mock object created by the patch decorator.
        patched_check.return_value = True  # sets the return value of the patched_check mock object to True. This means that whenever the check method is called during the test, it will return True instead of executing its actual implementation. This is done to simulate the behavior of the check method without actually running it. 
        # hardcoding the value to True in the actual implementation would be problematic because it would not accurately reflect the real state of the database. The purpose of setting patched_check.return_value = True in the test is to simulate a scenario where the database is ready, allowing you to test the behavior of the wait_for_db command under controlled conditions.
        call_command('wait_for_db')  # This line calls the wait_for_db management command using the call_command function. This is the command being tested.
        patched_check.assert_called_once(database=['default'])  # The line patched_check.assert_called_once_with(database=['default']) is an assertion in the test that verifies the behavior of the wait_for_db management command. Passing database as an argument.

    # this function is used to test the wait_for_db command when the database is not ready. since db is not ready we will get an operational error
    # we will apply delay
    @patch('time.sleep')  # patch will ben applied on this function only
    def test_wait_for_db_delay(self,patched_sleep,patched_check):  # order of the arguments must be same as the order of the decorators
        patched_check.side_effect = [psycopg2Error]*2 + [OperationalError]*3 + [True]  # returning true at 6th time hoping db will be ready by then
        # explain
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count,6)
        patch.assert_called_with(database=['default'])


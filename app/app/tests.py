"""run sample tests"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):     # made test class that inherits from SimpleTestCase
    def test_add(self):              # naming should strart with "test_"
        res=calc.add(3,8)            # calls the add function from calc.py
        self.assertEqual(res,11)     # checks whether the res is as expected or not

    def test_subtract(self):
        res=calc.subtract(15,10)
        self.assertEqual(res,5)   
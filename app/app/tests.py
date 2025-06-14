"""Sample tests"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding nos together"""
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_substract_number(self):
        """Test substraction"""
        res = calc.substract(10,15)

        self.assertEqual(res, 5)
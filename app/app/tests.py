"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class TestCalc(SimpleTestCase):
    def test_add(self):
        res = calc.add(1, 2)
        self.assertEqual(res, 3)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)

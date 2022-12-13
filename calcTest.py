import unittest
from main import calc

class calcTest(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calc('3 + 4'), 7)

    def test_minus(self):
        self.assertEqual(calc('4 - 3'), 1)

#     def test_mult(self):
#         self.assertEqual(calc('3 * 4'), 12)

#     def test_div(self):
#         self.assertEqual(calc('10 / 5'), 2)

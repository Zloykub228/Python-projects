import unittest
from main import *

a = 7
b = 6
class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2), 4)
    def test_kwargs(self):
        self.assertEqual(adder(a, b), 13)
    def mixed_test(self):
        self.assertEqual(adder(1, c=2), 3)
    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, y, x), 5)
    def test_datatype(self):
        self.assertEqual(adder(5, 0, 10), 15)

if __name__ == "__main__":
    unittest.main()
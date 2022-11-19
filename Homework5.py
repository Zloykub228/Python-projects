import unittest
import time
from main import *
a=int(input('a= '))
b=int(input('b= '))

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(a, b), 10)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    unittest.main()


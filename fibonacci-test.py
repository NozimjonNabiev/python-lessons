import unittest
from functionserrors import fibonacci_nums

class fibonacci_numsTest(unittest.TestCase):
    def test_fibonacci_nums(self):
        self.assertEqual(fibonacci_nums(4), False)
        self.assertEqual(fibonacci_nums(1597), True)
        
    def test_fibonacci_num(self):
        self.assertEqual(fibonacci_nums(60), False)
        self.assertEqual(fibonacci_nums(2178309), True)

unittest.main()
import unittest
from functionserrors import even_numbers

class even_numbersTest(unittest.TestCase):
    def test_even_numbers(self):
        nums = [10,2,4,5,7,11,100]
        result = [10,2,4,100]
        self.assertEqual(even_numbers(nums),result)

unittest.main()

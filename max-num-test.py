import unittest
from functionserrors import eng_kattasi

class eng_kattasiTest(unittest.TestCase):
    def test_max(self):
        self.assertEqual(eng_kattasi(10,45,20), 45)
        self.assertEqual(eng_kattasi(-80,10,100), 100)


unittest.main()
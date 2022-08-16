import unittest
from functionserrors import capital_letter

class capital_letterTest(unittest.TestCase):
    def test_capital_letter(self):
        # names = ['jahon', 'karim', 'qosim']
        # result = ['Jahon', 'Karim', 'Qosim']
        self.assertEqual(capital_letter(['jahon', 'karim', 'qosim']), ['Jahon', 'Karim', 'Qosim'] )


unittest.main()
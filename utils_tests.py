import unittest
import utils

class test_utils(unittest.TestCase):
    def test_reversed(self):
        c = utils.utils()
        self.assertEqual(c.reversed(52),25)
        self.assertEqual(c.reversed('52'),25)
        self.assertEqual(c.reversed(52.0),25)
    def test_formatter(self):
        c = utils.utils()
        self.assertEqual(c.formatter(10),('0b1010', '0o12'))
        self.assertEqual(c.formatter('10'),('0b1010', '0o12'))
        self.assertEqual(c.formatter(10.0),('0b1010', '0o12'))
unittest.main()

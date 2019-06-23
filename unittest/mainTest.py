import unittest
from userstories.jbUserStories import us01, us02

class Tests(unittest.TestCase):
    def test_us01(self):
        input = {'@I1@': {'BIRT': '7 MAR 2020'}, '@I2@': {'BIRT': '7 MAR 2019'}}
        output = {'@I1@': {'BIRT': '00 JAN 0000'}, '@I2@': {'BIRT': '7 MAR 2019'}}
        self.assertEqual(us01(input), output)

    def test_us02(self):
        input = {'@I1@': {'BIRT': '7 MAR 2018'}, '@I2@': {'BIRT': '7 MAR 2018'}}
        input2 = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'MARR': '6 MAR 2018'}}
        output = {'@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'MARR': '00 JAN 0000'}}
        self.assertEqual(us02(input, input2), output)

unittest.main()

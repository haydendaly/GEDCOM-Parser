import unittest
from userstories.jbUserStories import us01, us02
from userstories.hdUserStories import us_35, us_36

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
        
    def test_us35(self):
        input = {'@I1@': {'NAME' : 'Hayden /Daly/', 'BIRT': '6 JUN 2019'}, '@I2@': {'NAME' : 'Todd /Daly/', 'BIRT': '7 MAR 2018'}}
        output = ['@I1@', 'Hayden /Daly/', '6 JUN 2019']
        self.assertEqual(us_35(input), output)

    def test_us36(self):
         input = {'@I1@': {'NAME' : 'Hayden /Daly/', 'DEAT': '6 JUN 2019'}, '@I2@': {'NAME' : 'Todd /Daly/', 'BIRT': '7 MAR 2018'}}
         output = ['@I1@', 'Hayden /Daly/', '6 JUN 2019']
         self.assertEqual(us_36(input), output)

unittest.main()

# Must run unitTest while in the unittest directory (more flexibility can be added in future refactors)
import sys
import os
sys.path.append(os.path.abspath('../userstories'))

from prettytable import PrettyTable;

import unittest
from jbUserStories import us01, us02, us04, us05
from hdUserStories import us35, us36, us29, us39
from gaUserStories import us38, us27, us30, us31

class Tests(unittest.TestCase):
    def test_us01(self):
        input = { 'individualData': {'@I1@': { 'NAME': 'Date After Current /Date/', 'BIRT': '2020-03-07', 'DEAT': 'N/A'}, '@I2@': { 'NAME': 'Valid /Date/', 'BIRT': '2019-03-07', 'DEAT': 'N/A'} }, 'familyData': {} }

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Date Tag', 'Date']
        testTable.add_row(['@I1@', 'Date After Current /Date/', 'BIRT', '2020-03-07' ])
        testTableEmp = PrettyTable()
        testTableEmp.field_names = ['FAM ID', 'Date Tag', 'Date']

        output = { 'invalidIndiDates': testTable.get_string(), 'invalidFamDates': testTableEmp.get_string() }
        self.assertEqual(us01(input), output)

    def test_us02(self):
        input = {'individualData': {'@I1@': {'NAME': 'HUSB', 'BIRT': '2018-03-07'}, '@I2@': {'NAME': 'WIFE', 'BIRT': '2018-03-07'} }, 'familyData': {'@F1@': {'HUSB': '@I1@', 'HUSB_NAME': 'HUSB', 'WIFE': '@I2@', 'WIFE_NAME': 'WIFE', 'MARR': '2018-03-06'}} }

        testTable = PrettyTable()
        testTable.field_names = ['FAM ID', 'Married', 'Husband ID', 'Husband Name', 'Husband Birthday', 'Wife ID', 'Wife Name', 'Wife Birthday']
        testTable.add_row(['@F1@', '2018-03-06', '@I1@', 'HUSB', '2018-03-07', '@I2@', 'WIFE', '2018-03-07' ])

        output = testTable
        self.assertEqual(us02(input).get_string(), output.get_string())

    def test_us04(self):
        input = {'individualData': {'@I1@': {'NAME': 'HUSB', 'BIRT': '2018-03-07'}, '@I2@': {'NAME': 'WIFE', 'BIRT': '2018-03-07'} }, 'familyData': {'@F1@': {'HUSB': '@I1@', 'HUSB_NAME': 'HUSB', 'WIFE': '@I2@', 'WIFE_NAME': 'WIFE', 'MARR': '2018-03-06', 'DIV': '2018-03-05'}} }

        testTable = PrettyTable()
        testTable.field_names = ['FAM ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name']
        testTable.add_row(['@F1@', '2018-03-06', '2018-03-05', '@I1@', 'HUSB', '@I2@', 'WIFE'])

        output = testTable
        self.assertEqual(us04(input).get_string(), output.get_string())

    def test_us05(self):
        input = {'individualData': {'@I1@': {'NAME': 'HUSB', 'DEAT': '2018-03-07'}, '@I2@': {'NAME': 'WIFE', 'DEAT': '2018-03-05'} }, 'familyData': {'@F1@': {'HUSB': '@I1@', 'HUSB_NAME': 'HUSB', 'WIFE': '@I2@', 'WIFE_NAME': 'WIFE', 'MARR': '2018-03-06'}} }

        testTable = PrettyTable(maxDiff=None)
        testTable.field_names = ['FAM ID', 'Married', 'Husband ID', 'Husband Name', 'Husband Death', 'Wife ID', 'Wife Name', 'Wife Death']
        testTable.add_row(['@F1@', '2018-03-06', '@I1@', 'HUSB', '2018-03-07', '@I2@', 'WIFE', '2018-03-05' ])

        output = testTable
        self.assertEqual(us05(input).get_string(), output.get_string())

    def test_us35(self):
        input = { 'individualData': {'@I1@': {'NAME' : 'Hayden /Daly/', 'BIRT': '2019-07-06'}, '@I2@': {'NAME' : 'Todd /Daly/', 'BIRT': '2018-03-07'}} }

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday']
        testTable.add_row(['@I1@', 'Hayden /Daly/', '2019-07-06'])

        output = testTable
        self.assertEqual(us35(input).get_string(), output.get_string())

    def test_us36(self):
        input = { 'individualData': {'@I1@': {'NAME' : 'Hayden /Daly/', 'DEAT': '2019-07-06'}, '@I2@': {'NAME' : 'Todd /Daly/', 'BIRT': '2019-03-07', 'DEAT': 'N/A'} } }

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Death']
        testTable.add_row(['@I1@', 'Hayden /Daly/', '2019-07-06'])

        output = testTable
        self.assertEqual(us36(input).get_string(), output.get_string())

    def test_us38(self):
        input = { 'individualData': {'@I1A': {'NAME' : 'Not /Upcoming/ /Birthday/', 'BIRT': '1999-10-29', 'ALIVE': 'True'}, '@I2@': {'NAME': 'Upcoming /Birthday/', 'BIRT': '1999-07-30', 'ALIVE': 'True'} } }

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday']
        testTable.add_row(['@I2@', 'Upcoming /Birthday/', '1999-07-30'])

        output = testTable
        self.assertEqual(us38(input).get_string(), output.get_string())

    def test_us27(self):
        output = '19'
        self.assertEqual(us27('1999-10-29', 'N/A', 'True'), output)

    def test_us27_2(self):
        output = '100'
        self.assertEqual(us27('1800-01-01', '1900-01-01', 'False'), output)

    def test_us27_3(self):
        output = '100'
        self.assertEqual(us27('1800-01-01', '1900-01-01', 'False'), output)

    def test_us30(self):
        inputDict = {
            'individualData': {
                '@US30_01@': {
                    'NAME': 'Deceased Married /Person/',
                    'ALIVE': 'False',
                    'FAMS': [ '@US30@' ]
                },
                '@US30_02@': {
                    'NAME': 'Living Married /Person/',
                    'ALIVE': 'True',
                    'FAMS': [ '@US30@' ]
                }
            },
            'familyData': {
                '@US30@': {
                    'DIV': 'N/A'
                }
            }
        }

        expectedOutputTable = PrettyTable()
        expectedOutputTable.field_names = [ 'ID', 'Name' ]
        expectedOutputTable.add_row( [ '@US30_02@', 'Living Married /Person/' ] )

        self.assertEqual( us30( inputDict ).get_string(), expectedOutputTable.get_string() )

    def test_us31(self):
        inputDict = {
            'individualData': {
                '@US31_01@': {
                    'NAME': 'Deceased Single /Person/',
                    'ALIVE': 'False',
                    'AGE': 'N/A',
                    'FAMS': 'N/A'
                },
                '@US31_02@': {
                    'NAME': 'Living Single /Person/ Over 30',
                    'ALIVE': 'True',
                    'AGE': '40',
                    'FAMS': 'N/A'
                },
                '@US31_03@': {
                    'NAME': 'Living Single /Person/ Under 30',
                    'ALIVE': 'True',
                    'AGE': '29',
                    'FAMS': 'N/A'
                }
            },
            'familyData': { }
        }

        expectedOutputTable = PrettyTable()
        expectedOutputTable.field_names = [ 'ID', 'Name' ]
        expectedOutputTable.add_row( [ '@US31_02@', 'Living Single /Person/ Over 30' ] )

        self.assertEqual( us31( inputDict ).get_string(), expectedOutputTable.get_string() )

    def test_us29(self):
        input = { 'individualData': {'@I1@': {'NAME' : 'Hayden /Daly/', 'DEAT': '2019-06-06'}, '@I2@': {'NAME' : 'Todd /Daly/', 'BIRT': '2019-03-07', 'DEAT': 'N/A'} } }

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name']
        testTable.add_row(['@I1@', 'Hayden /Daly/'])

        output = testTable
        self.assertEqual(us29(input).get_string(), output.get_string())

    def test_us39(self):
        input = { 'familyData' : {'@F1@': {'MARR': '2017-07-10', 'HUSB_NAME': 'Todd /Daly/', 'WIFE_NAME': 'Amy /Fisher/'}, '@F2@': {'MARR': '1962-06-14', 'HUSB_NAME': 'Lee /Daly/', 'WIFE_NAME': 'Betty /Berardini/'} } }

        testTable = PrettyTable()
        testTable.field_names = ['Family ID', 'Husband', 'Wife', 'Marriage Date' ]
        testTable.add_row(['@F1@', 'Todd /Daly/', 'Amy /Fisher/', '2017-07-10'])

        output = testTable
        self.assertEqual( us39( input ).get_string(), output.get_string())


unittest.main()

import datetime
from prettytable import PrettyTable

# Checks that Dates (birth, marriage, divorce, death) are not after the current date
def us01(GEDCOM_dict):

    invalidIndiDateTable = PrettyTable()
    invalidIndiDateTable.field_names = ['ID', 'Name', 'Date Tag', 'Date']

    for key, value in GEDCOM_dict['individualData'].items():
        today = datetime.datetime.now()
        if ( value['BIRT'] != 'N/A' ):
            if datetime.datetime.strptime(" ".join( value['BIRT'].split('-') ), '%Y %m %d') > today:
                invalidIndiDateTable.add_row([key, value['NAME'], 'BIRT', value['BIRT']])
        if ( value['DEAT'] != 'N/A' ):
            if datetime.datetime.strptime(" ".join( value['DEAT'].split('-') ), '%Y %m %d') > today:
                invalidIndiDateTable.add_row([key, value['NAME'], 'DEAT', value['DEAT']])

    invalidFamDateTable = PrettyTable()
    invalidFamDateTable.field_names = ['FAM ID', 'Date Tag', 'Date']
    for key, value in GEDCOM_dict['familyData'].items():
        today = datetime.datetime.now()
        if ( value['MARR'] != 'N/A' ):
            if datetime.datetime.strptime(" ".join( value['MARR'].split('-') ), '%Y %m %d') > today:
                invalidFamDateTable.add_row([key, 'MARR', value['MARR']])
        if ( value['DIV'] != 'N/A' ):
            if datetime.datetime.strptime(" ".join( value['DIV'].split('-') ), '%Y %m %d') > today:
                invalidFamDateTable.add_row([key, 'DIV', value['DIV']])

    return { 'invalidIndiDates' : invalidIndiDateTable.get_string(), 'invalidFamDates' : invalidFamDateTable.get_string() }

# Checks that Birth occur before marriage of an individual
def us02(GEDCOM_dict):

    invalidDateTable = PrettyTable()
    invalidDateTable.field_names = ['FAM ID', 'Married', 'Husband ID', 'Husband Name', 'Husband Birthday', 'Wife ID', 'Wife Name', 'Wife Birthday']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']
    for key, value in familyData.items():
        if ( value['MARR'] != 'N/A' ):
            # Checks that the Husband's and Wife's Marriage Date does not occur before their respective birthdays
            marr_date = datetime.datetime.strptime(" ".join( value['MARR'].split('-') ), '%Y %m %d')
            if ( individualData[value['HUSB']]['BIRT'] != 'N/A' ):
                husb_birt = datetime.datetime.strptime(" ".join( individualData[value['HUSB']]['BIRT'].split('-') ), '%Y %m %d')
            else:
                husb_birt = datetime.datetime.min

            if ( individualData[value['WIFE']]['BIRT'] != 'N/A' ):
                wife_birt = datetime.datetime.strptime(" ".join( individualData[value['WIFE']]['BIRT'].split('-') ), '%Y %m %d')
            else:
                wife_birt = datetime.datetime.min

            if ( husb_birt >= marr_date or wife_birt >= marr_date ):
                invalidDateTable.add_row( [ key, value['MARR'], value['HUSB'], value['HUSB_NAME'], individualData[value['HUSB']]['BIRT'], value['WIFE'], value['WIFE_NAME'], individualData[value['WIFE']]['BIRT'] ] )

    return invalidDateTable

def us04(GEDCOM_dict):
    invalidDateTable = PrettyTable()
    invalidDateTable.field_names = ['FAM ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name']

    familyData = GEDCOM_dict['familyData']
    # individualData = GEDCOM_dict['individualData']
    for key, value in familyData.items():
        # marr_date = datetime.datetime.strptime(" ".join( value['MARR'].split('-') ), '%Y %m %d')
        if ( value['MARR'] != 'N/A' ):
            if value['DIV'] != 'N/A':
                if datetime.datetime.strptime(" ".join( value['MARR'].split('-') ), '%Y %m %d') > datetime.datetime.strptime(" ".join( value['DIV'].split('-') ), '%Y %m %d'):
                    invalidDateTable.add_row([ key, value['MARR'], value['DIV'], value['HUSB'], value['HUSB_NAME'], value['WIFE'], value['WIFE_NAME']])
    return invalidDateTable

def us05(GEDCOM_dict):
    invalidDateTable = PrettyTable()
    invalidDateTable.field_names = ['FAM ID', 'Married', 'Husband ID', 'Husband Name', 'Husband Death', 'Wife ID', 'Wife Name', 'Wife Death']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']
    for key, value in familyData.items():
        if ( value['MARR'] != 'N/A' ):
            marr_date = datetime.datetime.strptime(" ".join( value['MARR'].split('-') ), '%Y %m %d')
            if (individualData[value['HUSB']]['DEAT'] != 'N/A'):
                husb_deat = datetime.datetime.strptime(" ".join( individualData[value['HUSB']]['DEAT'].split('-') ), '%Y %m %d')
            else:
                husb_deat = datetime.datetime.min

            if (individualData[value['WIFE']]['DEAT'] != 'N/A'):
                wife_deat = datetime.datetime.strptime(" ".join( individualData[value['WIFE']]['DEAT'].split('-') ), '%Y %m %d')
            else:
                wife_deat = datetime.datetime.min

            if (husb_deat >= marr_date or wife_deat >= marr_date):
                    invalidDateTable.add_row([ key, value['MARR'], value['HUSB'], value['HUSB_NAME'], husb_deat, value['WIFE'], value['WIFE_NAME'], wife_deat])
    return invalidDateTable

import datetime
import prettytable

# [Sprint02] List all deceased individuals in a GEDCOM file
def us29(GEDCOM_dict):

    deadTable = prettytable.PrettyTable()
    deadTable.field_names = ["ID", "Name"]

    for key, value in GEDCOM_dict['individualData'].items():
        if ( value['DEAT'] and value['DEAT'] != 'N/A' ):
            row = [key, value['NAME']]
            deadTable.add_row(row)

    return deadTable

# [Sprint01] List all people in a GEDCOM file who were born in the last 30 days
def us35(GEDCOM_dict):

    recentBirtTable = prettytable.PrettyTable()
    recentBirtTable.field_names = ['ID', 'Name', 'Birthday']

    for key, value in GEDCOM_dict['individualData'].items():
        if ( value['BIRT'] and value['BIRT'] != 'N/A' ):
            birthdate = datetime.datetime.strptime(" ".join( value['BIRT'].split('-') ), '%Y %m %d')
            today = datetime.datetime.now()

            if( birthdate >= today + datetime.timedelta(-30) and birthdate <= today ):
                row = [key, value['NAME'], value['BIRT']]
                recentBirtTable.add_row(row)

    return recentBirtTable

# [Sprint01] List all people in a GEDCOM file who died in the last 30 days
def us36(GEDCOM_dict):

    recentDeatTable = prettytable.PrettyTable()
    recentDeatTable.field_names = ["ID", "Name", "Death"]

    for key, value in GEDCOM_dict['individualData'].items():
        if ( value['DEAT'] and value['DEAT'] != 'N/A' ):
            deathdate = datetime.datetime.strptime(" ".join(value['DEAT'].split('-') ), '%Y %m %d')
            today = datetime.datetime.now()
            if( deathdate >= today + datetime.timedelta(-30) and deathdate <= today ):
                row = [key, value['NAME'], value['DEAT']]
                recentDeatTable.add_row(row)

    return recentDeatTable

# [Sprint02] List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
def us39(GEDCOM_dict):

    upcomingAnniversariesTable = prettytable.PrettyTable()
    upcomingAnniversariesTable.field_names = ["Family ID", "Husband", "Wife", "Marriage Date"]

    for key, value in GEDCOM_dict['familyData'].items():
        if ( value['MARR'] and value['MARR'] != 'N/A' ):
            marriagedate = datetime.datetime.strptime(" ".join(value['MARR'].split('-') ), '%Y %m %d')
            marriagedate = marriagedate.replace(year=2019)
            today = datetime.datetime.now()

            if( marriagedate <= today + datetime.timedelta(30)) and marriagedate >= today:
                row = [key, value['HUSB_NAME'], value['WIFE_NAME'], value['MARR']]
                upcomingAnniversariesTable.add_row(row)

    return upcomingAnniversariesTable

import datetime
import prettytable

def us29(GEDCOM_dict):

    deadTable = prettytable.PrettyTable()
    deadTable.field_names = ["ID", "Name"]

    for key, value in GEDCOM_dict['individualData'].items():
        if ( value['DEAT'] and value['DEAT'] != 'N/A' ):
            row = [key, value['NAME']]
            deadTable.add_row(row)

    return deadTable

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

def us39(familyData):
    for key in familyData:
        print(familyData[key])
    upcomingAnniversariesTable = familyData

    return upcomingAnniversariesTable

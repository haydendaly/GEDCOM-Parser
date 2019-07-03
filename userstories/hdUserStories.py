import datetime
import prettytable

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

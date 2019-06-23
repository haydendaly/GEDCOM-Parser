import unittest
import datetime
import prettytable

def us_35(individualData):
    try:
        recentBirtTable = prettytable.PrettyTable()
        recentBirtTable.field_names = ['ID', 'Name', 'Birthday']
    except:
        return 'No module \'PrettyTable\''

    bool = False
    rows = []

    for key, value in individualData.items():
        if(datetime.datetime.strptime(value['BIRT'], '%d %b %Y') > datetime.datetime.now() + datetime.timedelta(-30)):
            row = [key, value['NAME'], value['BIRT']]
            rows += row
            recentBirtTable.add_row(row)
            bool = True
    if bool == True:
        print('Born Within the Past 30 Days')
        print(recentBirtTable)
        return rows

def us_36(individualData):
    try:
        recentDeatTable = prettytable.PrettyTable()
        recentDeatTable.field_names = ["ID", "Name", "Death Date"]
    except:
        return 'No module \'PrettyTable\''

    bool = False
    rows = []

    for key, value in individualData.items():
        if 'DEAT' in value:
            if(datetime.datetime.strptime(value['DEAT'], '%d %b %Y') > datetime.datetime.now() + datetime.timedelta(-30)):
                row = [key, value['NAME'], value['DEAT']]
                rows += row
                recentDeatTable.add_row(row)
                bool = True
    if bool == True:
        print('Death Within the Past 30 Days')
        print(recentDeatTable)
        return rows

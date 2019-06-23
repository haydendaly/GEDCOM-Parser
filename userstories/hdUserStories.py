import unittest
import datetime
import prettytable

def us_35(individualData):
    try:
        recentBirtTable = prettytable.PrettyTable()
        recentBirtTable.field_names = ["ID", "Name", "Birthday"]
    except:
        print("No module 'PrettyTable'")

    bool = False

    for key, value in individualData.items():
        if(datetime.datetime.strptime(value['BIRT'], '%d %b %Y') > datetime.datetime.now() + datetime.timedelta(-30)):
            recentBirtTable.add_row([key, value['NAME'], value['BIRT']])
            bool = True
    if bool == True:
        print('Born Within the Past 30 Days')
        print(recentBirtTable)

def us_36(individualData):
    try:
        recentDeatTable = prettytable.PrettyTable()
        recentDeatTable.field_names = ["ID", "Name", "Death Date"]
    except:
        print("No module 'PrettyTable'")

    bool = False

    for key, value in individualData.items():
        if 'DEAT' in value:
            if(datetime.datetime.strptime(value['DEAT'], '%d %b %Y') > datetime.datetime.now() + datetime.timedelta(-30)):
                recentDeatTable.add_row([key, value['NAME'], value['DEAT']])
                bool = True
    if bool == True:
        print('Death Within the Past 30 Days')
        print(recentDeatTable)

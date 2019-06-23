import datetime

def us00(x):
    return x + 1

def us01(data):
    for key, value in data.items():
        if 'BIRT' in value:
            if datetime.datetime.strptime(value['BIRT'], '%d %b %Y') > datetime.datetime.now():
                value['BIRT'] = '00 JAN 0000'
        elif 'DEAT' in value:
            if datetime.datetime.strptime(value['DEAT'], '%d %b %Y') > datetime.datetime.now():
                value['DEAT'] = '00 JAN 0000'
        elif 'MARR' in value:
            if datetime.datetime.strptime(value['MARR'], '%d %b %Y') > datetime.datetime.now():
                value['MARR'] = '00 JAN 0000'
        elif 'DIV' in value:
            if datetime.datetime.strptime(value['DIV'], '%d %b %Y') > datetime.datetime.now():
                value['DIV'] = '00 JAN 0000'

    return data

def us02(individualData, familyData):
    for key, value in familyData.items():
        if 'MARR' in value:
            marr_date = datetime.datetime.strptime(value['MARR'], '%d %b %Y')
            husb_birt = datetime.datetime.strptime(individualData[value['HUSB']]['BIRT'], '%d %b %Y')
            wife_birt = datetime.datetime.strptime(individualData[value['WIFE']]['BIRT'], '%d %b %Y')

            if husb_birt >= marr_date:
                value['MARR'] = '00 JAN 0000'
            elif wife_birt >= marr_date:
                value['MARR'] = '00 JAN 0000'

    return familyData

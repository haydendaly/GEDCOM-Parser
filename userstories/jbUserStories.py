import datetime

def us01(data):
    for key, value in data.items():
        if datetime.datetime.strptime(value['BIRT'], '%d %b %Y') > datetime.datetime.now():
            value['BIRT'] = '99 DEC 9999'
            print('Invalid Date' + ' ' + value['BIRT'])
        elif 'DEAT' in value:
            if datetime.datetime.strptime(value['DEAT'], '%d %b %Y') > datetime.datetime.now():
                value['DEAT'] = '99 DEC 9999'
        elif 'MARR' in value:
            if datetime.datetime.strptime(value['MARR'], '%d %b %Y') > datetime.datetime.now():
                value['MARR'] = '99 DEC 9999'
        elif 'DIV' in value:
            if datetime.datetime.strptime(value['DIV'], '%d %b %Y') > datetime.datetime.now():
                value['DIV'] = '99 DEC 9999'

    return data


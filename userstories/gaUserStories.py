# /*******************************************************************************
#  Name			: Gil Gerard Austria
#  Author		: Gil Gerard Austria
#  Date			: 2019-06-24
#  Description	: Project 04 -  Sprint 1
#  Pledge		:"I pledge my honor that I have abided by the Stevens Honor System"	- Gil Gerard Austria
#  *******************************************************************************/

import datetime

from prettytable import PrettyTable
from natsort import natsorted

# ----------------------------------- Sprint 01 -----------------------------------
# List all upcoming birthdays
def us38(GEDCOM_dict):

    birthdayDict = {}   # Dict used to hold data to be passed into us_38 to find upcoming birthdays

    individualData = GEDCOM_dict['individualData']
    idListSorted = natsorted( individualData.keys() )

    for id in idListSorted:
        name = individualData[id]['NAME']
        alive = individualData[id]['ALIVE']
        birthday = individualData[id]['BIRT']
        if ( alive == 'True' ):
            birthdayDict[id] = { 'NAME' : name, 'BIRT' : birthday }
        else:
            continue

    upcomingBirthdayTable = PrettyTable()
    upcomingBirthdayTable.field_names = ["ID", "Name", "Birthday"]

    for id in birthdayDict:

        birthdate = str(birthdayDict[id].get('BIRT'))
        if ( birthdate != 'N/A' ):
            birthdateSplit = birthdate.split('-')
            birthMonth = int(birthdateSplit[1])
            birthDayDate = int(birthdateSplit[2])

            today = datetime.datetime.today()
            currentYear = today.year
            currentMonth = today.month
            currentDay = today.day

            birthdayThisYear = datetime.datetime( currentYear, birthMonth, birthDayDate )

            if ( birthdayThisYear > today and birthdayThisYear < today + datetime.timedelta(30) ):
                upcomingBirthdayTable.add_row([id, birthdayDict[id].get('NAME'), birthdayDict[id].get('BIRT')])

    return upcomingBirthdayTable


# Display Individual Age
def us27(birthday, death, alive):

    if ( birthday != 'N/A' and death != 'N/A' and alive == 'False'):  # Birth and Death Date are Known (alive == 'False')
        #do date arithmetic
        birthdateSplit = birthday.split('-')
        birthMonth = str(birthdateSplit[1])
        birthDayDate = str(birthdateSplit[2])
        birthYear = str(birthdateSplit[0])

        deathdateSplit = death.split('-')
        deathMonth = str(deathdateSplit[1])
        deathDayDate = str(deathdateSplit[2])
        deathYear = str(deathdateSplit[0])

        birthDate = birthYear + birthMonth + birthDayDate
        deathDate = deathYear + deathMonth + deathDayDate

        age = int(deathDate) - int(birthDate)

        if ( age < 0 ):
            return 'N/A'

        return str(age).zfill(7)[:-4].lstrip('0').zfill(1)


    if ( birthday != 'N/A' and death == 'N/A' and alive == 'True' ): # BirthDay is known and alive == 'True', no death date
        #do date arithmetic
        birthdateSplit = birthday.split('-')
        birthMonth = str(birthdateSplit[1])
        birthDayDate = str(birthdateSplit[2])
        birthYear = str(birthdateSplit[0])
        birthDate = birthYear + birthMonth + birthDayDate

        today = datetime.datetime.today()
        dateToday = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2)

        age = int(dateToday) - int(birthDate)

        if ( age < 0 ):
            return 'N/A'

        return str(age).zfill(7)[:-4].lstrip('0').zfill(1)

    if ( birthday == 'N/A' ):
        # Cannot calculate age
        return 'N/A'

    return 'N/A'


# ----------------------------------- Sprint 02 -----------------------------------

# List all living married people in a GEDCOM file
def us30(GEDCOM_dict):

    livingMarriedTable = PrettyTable()
    livingMarriedTable.field_names = [ 'ID', 'Name' ]

    individualData = GEDCOM_dict['individualData']
    familyData = GEDCOM_dict['familyData']
    idListSorted = natsorted( individualData.keys() )

    for id in idListSorted:
        if ( individualData[id]['ALIVE'] == 'True' ):
            if ( individualData[id]['FAMS'] == 'N/A' ):
                continue
            else:
                fams = individualData[id]['FAMS']
                for famId in fams:
                    if ( familyData[ famId ]['DIV'] == 'N/A' ):
                        livingMarriedTable.add_row( [ id, individualData[id]['NAME'] ] )
                    else:
                        continue
        else:
            continue

    return livingMarriedTable

# List all living people over 30 who have never been married in a GEDCOM file
def us31(GEDCOM_dict):

    livingSingleTable = PrettyTable()
    livingSingleTable.field_names = [ 'ID', 'Name' ]

    individualData = GEDCOM_dict['individualData']
    idListSorted = natsorted( individualData.keys() )

    for id in idListSorted:
        if ( individualData[id]['ALIVE'] == 'True' ):
            if ( individualData[id]['FAMS'] == 'N/A' ):
                if ( individualData[id]['AGE'] != 'N/A' and int(individualData[id]['AGE']) >= 30 ):
                    livingSingleTable.add_row( [ id, individualData[id]['NAME'] ] )
                else:
                    continue
            else:
                continue
        else:
            continue

    return livingSingleTable

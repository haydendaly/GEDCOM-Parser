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
        birthMonth = int(birthdateSplit[1])
        birthDayDate = int(birthdateSplit[2])
        birthYear = int(birthdateSplit[0])

        deathdateSplit = death.split('-')
        deathMonth = int(deathdateSplit[1])
        deathDayDate = int(deathdateSplit[2])
        deathYear = int(deathdateSplit[0])

        birthDate = datetime.datetime( birthYear, birthMonth, birthDayDate )
        deathDate = datetime.datetime( deathYear, deathMonth, deathDayDate )
        ageInYears = deathDate.year - birthYear
        if ( deathDate.month < birthMonth ):
            return ageInYears >= 0 if ageInYears else 'N/A'
        elif ( deathDate.month == birthMonth ):
            if ( deathDate.day < int( birthdateSplit[0] ) ):
                return ageInYears >= 0 if ageInYears else 'N/A'
            elif ( deathDate.day >= int( birthdateSplit[0] ) ):
                return ageInYears + 1 >= 0 if ageInYears + 1 else 'N/A'
        else:
            return ageInYears + 1 >= 0 if ageInYears + 1 else 'N/A'

    if ( birthday != 'N/A' and death == 'N/A' and alive == 'True' ): # BirthDay is known and alive == 'True', no death date
        #do date arithmetic
        birthdateSplit = birthday.split('-')
        birthMonth = int(birthdateSplit[1])
        birthDayDate = int(birthdateSplit[2])
        birthYear = int(birthdateSplit[0])

        birthDate = datetime.datetime( birthYear, birthMonth, birthDayDate )
        dateToday = datetime.datetime.today()
        ageInYears = dateToday.year - birthYear
        if ( dateToday.month < birthMonth ):
            return ageInYears >= 0 if ageInYears else 'N/A'
        elif ( dateToday.month == birthMonth ):
            if ( dateToday.day < int( birthdateSplit[0] ) ):
                return ageInYears >= 0 if ageInYears else 'N/A'
            elif ( dateToday.day >= int( birthdateSplit[0] ) ):
                return ageInYears + 1 >= 0 if ageInYears + 1 else 'N/A'
        else:
            return ageInYears + 1 >= 0 if ageInYears + 1 else 'N/A'

    if ( birthday == 'N/A' ):
        # Cannot calculate age
        return 'N/A'

    return 'N/A'
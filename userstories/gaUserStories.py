# /*******************************************************************************
#  Name			: Gil Gerard Austria
#  Author		: Gil Gerard Austria
#  Date			: 2019-06-24
#  Description	: Project 04 -  Sprint 1
#  Pledge		:"I pledge my honor that I have abided by the Stevens Honor System"	- Gil Gerard Austria
#  *******************************************************************************/

import datetime
from prettytable import PrettyTable


# List all upcoming birthdays
def us_38(birthdayDict):

  upcomingBirthdayLst = []

  print('Upcoming Birthdays')

  try:
    upcomingBirthdayTable = PrettyTable()
    upcomingBirthdayTable.field_names = ["ID", "Name", "Birthday"]

  except:
    print("No module 'PrettyTable'")

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
      upcomingBirthdayLst.append([id, birthdayDict[id].get('NAME'), birthdayDict[id].get('BIRT')])

  print(upcomingBirthdayTable)

  return upcomingBirthdayLst


# Display Individual Age
def us_27(birthday, death, alive):

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
        return ageInYears
    elif ( deathDate.month == birthMonth ):
        if ( deathDate.day < int( birthdateSplit[0] ) ):
            return ageInYears
        elif ( deathDate.day >= int( birthdateSplit[0] ) ):
            return ageInYears + 1
    else:
        return ageInYears + 1

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
        return ageInYears
    elif ( dateToday.month == birthMonth ):
        if ( dateToday.day < int( birthdateSplit[0] ) ):
            return ageInYears
        elif ( dateToday.day >= int( birthdateSplit[0] ) ):
            return ageInYears + 1
    else:
        return ageInYears + 1

  if ( birthday == 'N/A' ):
    # Cannot calculate age
    return 'N/A'

  return 'N/A'
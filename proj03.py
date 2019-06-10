# /*******************************************************************************
#  Author		: Gil Gerard Austria, Justin Bernstein, Hayden Daly
#  Date			: 2019-06-09
#  Description	: Project 03
#  Github       : https://github.com/haydendaly/GEDCOM-Parser
#  Pledge		:"I pledge my honor that I have abided by the Stevens Honor System"	- Gil Gerard Austria, Justin Bernstein, Hayden Daly
#  *******************************************************************************/

import sys
from datetime import date
from prettytable import PrettyTable
from natsort import natsorted

validTagLevelPairs = {
    'INDI': 0,
    'FAM': 0,
    'HEAD': 0,
    'TRLR': 0,
    'NOTE': 0,
    'NAME': 1,
    'SEX': 1,
    'BIRT': 1,
    'DEAT': 1,
    'FAMC': 1,
    'FAMS': 1,
    'MARR': 1,
    'HUSB': 1,
    'WIFE': 1,
    'CHIL': 1,
    'DIV': 1,
    'DATE': 2
}

uniqueTags = ['INDI', 'FAM']
tagsWithDates = ['BIRT', 'DEAT', 'DIV', 'MARR']
tagsWithMultiplePossibleEntries = ['FAMS', 'CHIL']

def formatString(level, tag, validity, arguments):
    return str(level) + "|" + str(tag) + "|" + str(validity) + "|" + str(arguments)


def validate(line):
    lineSplit = line.split()

    # Parse Out Level and convert to int
    level = int(lineSplit[0])

    if (level == 0):    # Special Case because we need to parse INDI/FAM tags differently
        if(lineSplit[1] in uniqueTags):
            # Case where INDI/FAM tag appear in the wrong order
            return formatString(level, lineSplit[1], "N", " ".join(lineSplit[2:]))
        else:
            # Case of a Correctly Ordered INDI/FAM tag
            if (len(lineSplit) >= 3 and lineSplit[2] in uniqueTags):
                tag = lineSplit[2]
                arguments = lineSplit[1]
            else:   # Case of a Correctly Ordered HEAD, NOTE, or TRLR tag
                tag = lineSplit[1]
                arguments = " ".join(lineSplit[2:])
    # Else Case of a Correctly Ordered level 1 or level 2 tags (there are no tags in level 1 or 2 that differ from the <level> <tag> <args> format)
    else:
        # Case where the INDI/FAM tag is formatted correctly but has the wrong level
        if (len(lineSplit) >= 3 and lineSplit[2] in uniqueTags):
            return formatString(level, lineSplit[2], "N", lineSplit[1])
        # Default case for a normal tag and level
        tag = lineSplit[1]
        arguments = " ".join(lineSplit[2:])

    # Case where level is not in between 0 and 2, inclusive
    if (level < 0 or level > 2):
        return formatString(level, tag, "N", arguments)
    # Case where parsed tag is not a valid tag that should be recognized by our program
    if (tag not in validTagLevelPairs.keys()):
        return formatString(level, tag, "N", arguments)
    # Case where tag does not appear
    if (validTagLevelPairs[tag] != level):
        return formatString(level, tag, "N", arguments)

    return formatString(level, tag, "Y", arguments)


monthToNumDict = {
    'JAN': '01',
    'FEB': '02',
    'MAR': '03',
    'APR': '04',
    'MAY': '05',
    'JUN': '06',
    'JUL': '07',
    'AUG': '08',
    'SEP': '09',
    'OCT': '10',
    'NOV': '11',
    'DEC': '12'
}

def displayIndiData(outputFile, individualData):
    print('Individuals')

    try:
        indiDataTable = PrettyTable()
        indiDataTable.field_names = ["ID", "Name", "Gender", "Birthday", "Alive", "Death", "Child", "Spouse"]

    except:
        print("No module 'PrettyTable'")

    try:
        idListSorted = natsorted( individualData.keys() )
    except:
        print("No module 'natsort'")

    for id in idListSorted:
        indiData = individualData[ id ]

        name = indiData['NAME']
        gender = indiData['SEX']

        try:
            child = '{\'' + indiData['FAMC'] + '\'}'
        except:
            child = 'None'

        try:
            if ( len( indiData['FAMS'] ) == 1 ):
                spouse = '{\'' + "".join( indiData['FAMS'] ) + '\'}'
            else:
                spouse = '{\'' + "', '".join( indiData['FAMS'] ) + '\'}'
        except:
            spouse = 'N/A'

        # Format Birth Date
        birthdate = indiData['BIRT']
        birthdateSplit = birthdate.split(" ")
        birthday = birthdateSplit[2] + '-' + monthToNumDict[ birthdateSplit[1] ] + '-' + birthdateSplit[0].zfill(2)

        # Check if DEAT Tag Exists and Format Death Date
        if ( 'DEAT' in indiData.keys() ):
            alive = 'False'

            deathdate = indiData['DEAT']
            deathdateSplit = deathdate.split(" ")
            death = deathdateSplit[2] + '-' + monthToNumDict[ deathdateSplit[1] ] + '-' + deathdateSplit[0]
        else:
            alive = 'True'
            death = 'N/A'

        indiDataTable.add_row([id, name, gender, birthday, alive, death, child, spouse])

    print( indiDataTable )

    outputTable = open(outputFile, 'a')
    outputTable.write('Individuals\n')
    outputTable.write(indiDataTable.get_string())

    return

def displayFamData(outputFile, individualData, familyData):
    print('Families')

    try:
        famDataTable = PrettyTable()
        famDataTable.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

    except:
        print("No module 'PrettyTable'")

    try:
        idListSorted = natsorted( familyData.keys() )
    except:
        print("No module 'natsort'")

    for id in idListSorted:
        famData = familyData[id]

        try:
            # Format Married Date
            marriedDate = famData['MARR']
            marriedDateSplit = marriedDate.split(" ")
            married = marriedDateSplit[2] + '-' + monthToNumDict[ marriedDateSplit[1] ] + '-' + marriedDateSplit[0].zfill(2)
        except:
            married = 'N/A'

        # Check if Divorced and Format Death Date
        try:
            divorcedDate = famData['DIV']
            divorcedDateSplit = divorcedDate.split(" ")
            divorced = divorcedDateSplit[2] + '-' + monthToNumDict[ marriedDateSplit[1] ] + '-' + marriedDateSplit[0].zfill(2)
        except:
            divorced = 'N/A'

        # Get Husband Data
        try:
            husbandId = famData['HUSB']
            husbandName = individualData[husbandId].get('NAME')
        except:
            husbandId = 'N/A'
            husbandName = 'N/A'

        # Get Wife Data
        try:
            wifeId = famData['WIFE']
            wifeName = individualData[wifeId].get('NAME')
        except:
            wifeId = 'N/A'
            wifeName = 'N/A'

        # Check if Children Exist and Format Data
        try:
            if ( len( famData['CHIL'] ) == 1 ):
                children = '{\'' + "".join( famData['CHIL'] ) + '\'}'
            else:
                children = '{\'' + "\', \'".join( famData['CHIL'] ) + '\'}'
        except:
            children = 'None'

        famDataTable.add_row([id, married, divorced, husbandId, husbandName, wifeId, wifeName, children])

    print(famDataTable)

    outputTable = open(outputFile, 'a')
    outputTable.write('\nFamilies\n')
    outputTable.write(famDataTable.get_string())
    return


def parseValidDataForDisplay(outputFile, validLinesList):
    prevTopLevelTag = ""
    prevTopLevelId = ""
    individualData = {}
    familyData = {}
    prevTagPendingDate = ""
    tagsExcludedFromData = ['HEAD', 'NOTE', 'TRLR']

    for line in validLinesList:
        validLineSplit = line.split("|")
        tag = validLineSplit[1]
        arguments = validLineSplit[3]

        if ( tag in uniqueTags ):
            if ( tag == "INDI" ):
                individualData[ arguments ] = {}
            if ( tag == "FAM" ):
                familyData[ arguments ] = {}

            prevTopLevelTag = tag
            prevTopLevelId = arguments
        elif( tag in tagsExcludedFromData ):
            continue
        else:
            if ( prevTopLevelTag == "INDI" ):
                if ( tag not in tagsWithDates ):
                    if ( tag in tagsWithMultiplePossibleEntries ):
                        individualData[ prevTopLevelId ].update( { tag : [] } )
                        individualData[ prevTopLevelId ][ tag ].append( arguments )
                    elif ( tag == "DATE" ):
                        individualData[ prevTopLevelId ][ prevTagPendingDate ] = arguments
                    else:
                        individualData[ prevTopLevelId ].update( { tag : arguments } )
                else:
                    prevTagPendingDate = tag
                    individualData[ prevTopLevelId ].update( { tag: "" } )


            if ( prevTopLevelTag == "FAM" ):
                if ( tag not in tagsWithDates ):
                    if ( tag in tagsWithMultiplePossibleEntries ):
                        if ( tag not in familyData[ prevTopLevelId ].keys() ):
                            familyData[ prevTopLevelId ].update( { tag : [] } )
                        familyData[ prevTopLevelId ][ tag ].append( arguments )
                    elif ( tag == "DATE" ):
                        familyData[ prevTopLevelId ][ prevTagPendingDate ] = arguments
                    else:
                        familyData[ prevTopLevelId ].update( { tag : arguments } )
                else:
                    prevTagPendingDate = tag
                    familyData[ prevTopLevelId ].update( { tag: "" } )

    displayIndiData(outputFile, individualData)
    displayFamData(outputFile, individualData, familyData)
    return


def main(fileName):
    output = open(fileName[:-4]+'_output.txt', 'w+')
    inputFile = open(fileName, 'r')

    validLinesList = []

    for line in inputFile:
        output.write('--> ' + line.rstrip() + "\n")
        lineValidation = validate(line)
        output.write('<-- ' + lineValidation + "\n")
        validLinesList.append(lineValidation)

    tableTxtName = fileName[:-4]+'_INDI_AND_FAM_DATA_TABLE_output.txt'
    outputTable = open(tableTxtName, 'w+')
    parseValidDataForDisplay(tableTxtName, validLinesList)

    return


if __name__ == '__main__':
    main(sys.argv[1])

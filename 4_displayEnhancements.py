# /*******************************************************************************
#  Author		: Gil Gerard Austria, Justin Bernstein, Hayden Daly
#  Date			: 2019-06-09
#  Version      : Sprint.02.Proj.06
#  Description	: Using Functions Imported from UserStories, displays Additional Data about Individuals and Families
#                 Creates/Appends to Txt file ( {fileName}_output.txt )
#                 Returns Tables with Additional Data from User Story Enhancements
#  Github       : https://github.com/haydendaly/GEDCOM-Parser
#  Pledge		:"I pledge my honor that I have abided by the Stevens Honor System"	- Gil Gerard Austria, Justin Bernstein, Hayden Daly
#  *******************************************************************************/

# Built-in Python Modules
import sys
import json

# Non-Built-In Python Modules that Need to be Installed
from prettytable import PrettyTable

# Import userstories
from userstories import hdUserStories, jbUserStories, gaUserStories

# Enhancements:
#   us_27 (Implemented/Called Directly in 3_displayIndividualData.py)
#   us_28
#   us_29
#   us_30
#   us_31
#   us_34
#   us_35
#   us_36
#   us_38 -
#   us_39
#   us_40
#   us_41
def displayEnhancements(fileName, GEDCOM_dict):

    us_35 = hdUserStories.us_35(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write(us_35.get_string(title="[us_35] - Birth Within the Past 30 Days")+'\n\n')
    print('\n[us_35] Birth Within the Past 30 Days')
    print( us_35 )


    us_36 = hdUserStories.us_36(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write(us_36.get_string(title="[us_36] - Death Within the Past 30 Days")+'\n\n')
    print('\n[us_36] Death Within the Past 30 Days')
    print( us_36 )


    us_38 = gaUserStories.us_38(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write(us_38.get_string(title="[us_38] - Upcoming Birthdays")+'\n\n')
    print('\n[us_38] Upcoming Birthdays')
    print( us_38 )

    return

def main(fileName, GEDCOM_dict):

    # Case when the Program is Run Directly from Command Line and on an Valid Input File (Sanitized GEDCOM File from 1_sanitizedGEDCOM.py)
    if ( fileName.endswith('_dict.json') ):
        # READ FROM JSON DATA
        with open( fileName ) as GEDCOM_JSON:
            GEDCOM_dict = json.loads( GEDCOM_JSON.read() )

        displayEnhancements( fileName, GEDCOM_dict )

        return
    # Case when the Program is run from 0_main.py
    else:
        if ( len(GEDCOM_dict) != 0 ):
            displayEnhancements( fileName, GEDCOM_dict )

            return
        else:
            raise 'Empty Input, no GEDCOM Dictionary Data to Display'

    return


if __name__ == '__main__':
    main(sys.argv[1], {})
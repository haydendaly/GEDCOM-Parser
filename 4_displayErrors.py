# /*******************************************************************************
#  Author		: Gil Gerard Austria, Justin Bernstein, Hayden Daly
#  Date			: 2019-06-09
#  Version      : Sprint.02.Proj.06
#  Description	: Parses Dictionary Data to Output All Errors in Individuals and Families Using Functions Imported from UserStories
#                 Creates/Appends to Txt file ( {fileName}_output.txt )
#                 Returns Table with Individual Data
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

def displayErrors(fileName, GEDCOM_dict):

    us01 = jbUserStories.us01(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write('[us_01] - Error: Date Occurs After Current Date\n')
        output.write(us01['invalidIndiDates']+'\n\n')
        output.write(us01['invalidFamDates']+'\n\n')
    print('\n[us01] Error: Date Occurs AFter Current Date')
    print( us01 )


    us02 = jbUserStories.us02(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write('[us02] - Error: Date Occurs AFter Current Date\n')
        output.write(us02.get_string()+'\n\n')
    print('\n[us02] Error: Date Occurs AFter Current Date')
    print( us02 )


    return

def main(fileName, GEDCOM_dict):

    # Case when the Program is Run Directly from Command Line and on an Valid Input File (Sanitized GEDCOM File from 1_sanitizedGEDCOM.py)
    if ( fileName.endswith('_dict.json') ):
        # READ FROM JSON DATA
        with open( fileName ) as GEDCOM_JSON:
            GEDCOM_dict = json.loads( GEDCOM_JSON.read() )

        displayErrors( fileName, GEDCOM_dict )

        return
    # Case when the Program is run from 0_main.py
    else:
        if ( len(GEDCOM_dict) != 0 ):
            displayErrors( fileName, GEDCOM_dict )

            return
        else:
            raise 'Empty Input, no GEDCOM Dictionary Data to Display'

    return


if __name__ == '__main__':
    main(sys.argv[1], {})
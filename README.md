# Business Card OCR

This code is written in Python 3.

This program is designed to take the text of a business card as a string input and returns a ContactInfo object with the name, phone number and email address of the business card owner. 

## Instructions
To run the program, open a Bash command line window and enter the the following:

python3 ocr.py --document <business_card_text>

## Code Functionality
The code may dazzle you with the following capabilities:
* Parses names efficiently regardless of number of lines and order of text. 
* Ignores fax numbers when looking for a phone number.
* Disregards extraneous information such as addresses, company names and job titles.
* Does not confuse twitter handles with email addresses.

## Code Limitations
Despite these amazing capabilities, there are some features that have yet to be implemented, including:
* Support for multiple phone numbers (only one will be extracted, and this will be the phone number appearing in the lowest, i.e., closest to the bottom, line of the card).
* Ability to identify names for individual's whose work emails do not contain at least 4 characters of their name, or who do not have an email listed on their business card (future versions may use a first name api to identify names that are not otherwise found).
* Ability to reliably identify names, and not company names, in cases where a business card owner names a company after themselves (currently, the line in closest proximity to the email address would be identified as the name).
* Sensible error message that say what happened if information is not found.
 
## Testing the code
Automated unit testing might be great, but it is not included with this code. Instead, you can keep your copy and paste skills sharp by testing the following lines of code in your command line window.

All tests for this program are found below in this README. The tests include command line code inputs to copy and paste and expected outputs that should appear in the console. The commands are written with the assumption that the current directory contains the ocr.py file. If not, a file path will need to be added before the call to ocr.py.

### Test 1 (email before name, multiple numbers)

input:<br/>
python3 ocr.py --document "awilson@abctech.com\nArthur Wilson\nSoftware Engineer\nDecision & Security Technologies\nABC Technologies\n123 North 11th Street\nSuite 229\nArlington, VA 22209\nTel: +1 (703) 555-1259\nFax: +1 (703) 555-1200"

expected output:<br/>
Name: Arthur Wilson<br/>
Phone: 17035551259<br/>
Email: awilson@abctech.com

### Test 2 (email after name)

input: <br/>
python3 ocr.py --document "Foobar Technologies\n Analytic Developer \n Lisa Haung\n lisa.haung@foobartech.com \n 1234 Sentry Road\n Columbia, MD 12345\n Phone: 410-555-1234\n Fax: 410-555-4321"

expected output:<br/>
Name: Lisa Haung<br/>
Phone: 4105551234<br/>
Email: lisa.haung@foobartech.com

### Test 3 (fairly typical card)

input:<br/>
python3 ocr.py --document "ASYMMETRIK LTD\n Mike Smith\n Senior Software Engineer\n (410)555-1234\n msmith@asymmetrik.com"

expected output:<br/>
Name: Mike Smith<br/>
Phone: 4105551234<br/>
Email: msmith@asymmetrik.com

### Test 4 (missing phone number)

input: <br/>
python3 ocr.py --document "ASYMMETRIK LTD\n Mike Smith\n Senior Software Engineer\n Fax: (410)555-1234\n msmith@asymmetrik.com"

expected output:<br/>
Name: Mike Smith<br/>
Phone: None<br/>
Email: msmith@asymmetrik.com

### Test 5 (short email, expected failure of parser)

input: <br/>
python3 ocr.py --document "ASYMMETRIK LTD\n Bob Smith\n Senior Software Engineer\n (410)555-1234\nbob@asymmetrik.com"

expected output:<br/>
Name: None<br/>
Phone: 4105551234<br/>
Email: bob@asymmetrik.com

### Test 6 (twitter handle, multiple phone numbers)

input:<br/>
python3 ocr.py --document "Susie Smith\n @susiesmith\n office:3018959050\n cell:3039403856 \n ssmith@company.co"

expected output:<br/>
Name: Susie Smith<br/>
Phone: 3039403856<br/>
Email: ssmith@company.co

### Test 7 (no email)

input:<br/>
python3 ocr.py --document "Susie Smith\n @susiesmith\n office:3018959050\n cell:3039403856"

expected output:<br/>
Error: Email not found; cannot parse business card

### Test 8 (email and phone on same line)

input:<br/>
python3 ocr.py --document "Susie Smith\n @susiesmith\n cell:3039403856; ssmith@company.co"

expected output:<br/>
Name: Susie Smith<br/>
Phone: 3039403856<br/>
Email: ssmith@company.co

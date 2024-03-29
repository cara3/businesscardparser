import re
import argparse

def main():
    parser = argparse.ArgumentParser(description='Parse a business card')
    parser.add_argument('--document')
    args = vars(parser.parse_args())
    bc = BusinessCardParser
    ci = bc.getContactInfo(args)
    print('Name: ' + str(ci.getName()))
    print('Phone: ' + str(ci.getPhoneNumber()))
    print('Email: ' + str(ci.getEmailAddress()))
    return(ci)

def getEmailAddress(line):
    
    """
    Takes a line of text as input, assesses whether the text is an email address by checking for
    an @ symbol preceded by at least one character (to exclude twitter handles). Returns email if found.
    """
    if re.match('\@',line) == None:
        if re.search('\@',line):
            email = line
            return email
    
def getName(line, email):
    
    """
    Takes a line of text and an email address as inputs, finds all 4-character substrings
    in the first part of the email address (before @ symbol) and counts the number of email 
    substrings contained in the line of text. Returns name if at least one match between text and 
    email substrings is found.
    """
    
    if email != None:
        # extract first part of email, make line lowercase to prepare for match
        z = re.search('(\D*?)\@', email)
        email_start = z.group(1)
        line2 = line.lower()

        # find all four-character substrings in email_start
        email_strings = [email_start[i:i+4] for i in range(len(email_start)-4+1)]
        
        # look for at least one that matches
        x = 0
        for substring in email_strings:
            if re.search(substring, line2):
                x += 1
        
        if (x > 0) & (re.search('\@',line) == None):
            name = line
            return name
    
def getPhone(line):
    
    """
    Takes a line of text as an input and checks if it is a phone number by looking
    for a text string with at least 10 numeric digits that does not contain 
    the letter F (to exclude fax numbers).
    """
    
    if sum(x.isdigit() for x in line) >= 10:
        if not re.search('[Ff]', line):
            phone = re.sub('\D', '', line)
            return phone 

    
class BusinessCardParser:

    def __init__(self):
        return self

    def getContactInfo(document):
    
        """
        Takes a document string as an input. That string is assumed to contain
        contact information with different information items (e.g., name, email) separated by line
        breaks. The function calls other functions which identify the name, phone number and email 
        address from the contact information. These three items are then returned in a
        ContactInfo object.
        """
        
        # first change dict input to list and split lines
        lines = list(document.values())
        lines = lines[0].split("\\n")
        
        # reorder the list for efficiency (need to find email before name, most likely comes after name in line order)
        lines.reverse()
        
        # define starting value for variables
        email = None
        phone = None
        name = None
        
        for line in lines:
            
            # extract email
            if (email == None):
                email = getEmailAddress(line)
            
            # extract phone number
            if (phone == None):
                phone = getPhone(line)
            
            # extract name
            if ((name == None) & (email != None)):
                name = getName(line, email)
    
        # if re-order didn't work (i.e., email came before name), return to original line order and try again
        if ((name == None)):
            
            lines.reverse()

            for line in lines:
                
                # extract name
                if ((name == None) & (email != None)):
                    name = getName(line, email)
        
        # error handling - print error message if email not found
        if (email == None):
            print('Error: Caution! Email not found. Business card parsing not complete.')
        
        return ContactInfo(name, phone, email)

class ContactInfo:
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def getName(self):
        return self.name
    
    def getPhoneNumber(self):
        return self.phone
    
    def getEmailAddress(self):
        return self.email



if __name__ == "__main__":
    main()


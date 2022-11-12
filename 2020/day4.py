"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 4. 
    Problem description: https://adventofcode.com/2020/day/4
    Input: https://adventofcode.com/2020/day/4/input

    PART 1: Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
    PART 2: Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
"""
# Modules needed in this script.
import sys
import os
import re

# Passport class.
class Passport(object):

    byr = '' # Birth year
    iyr = '' # Issue Year
    eyr = '' # Expiration Year
    hgt = '' # Height
    hcl = '' # Hair Color
    ecl = '' # Eye Color
    pid = '' # Passport ID
    cid = '' # Country ID
    isValidPassport = False
    isValidDataPassport = False

    # Complete a information passport from a text line. 
    def completePassport(self, line):
        fields = line.split()
        for field in fields:
            paireValue = field.split(':')
            self.completeField(paireValue)

    #Complete an information field from text value.
    def completeField(self, paireValue):
            if 'byr' == paireValue[0]:
                self.byr = paireValue[1]
            elif 'iyr' == paireValue[0]:
                self.iyr = paireValue[1]
            elif 'eyr' == paireValue[0]:
                self.eyr = paireValue[1]
            elif 'hgt' == paireValue[0]:
                self.hgt = paireValue[1]
            elif 'hcl' == paireValue[0]:
                self.hcl = paireValue[1]
            elif 'ecl' == paireValue[0]:
                self.ecl = paireValue[1]
            elif 'pid' == paireValue[0]:
                self.pid = paireValue[1]
            elif 'cid' == paireValue[0]:
                self.cid = paireValue[1]

# Read a path and return a list where a line is an item.
def readFile(path):
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

# Found and complete the passport information from a text file.
def foundAllPassport(file):
    passportList = []

    if(file != None and len(file) > 0):

        passport = Passport()

        for line in file:
            if line == '\n' or line == '':
                checkIsValidatePassport(passport)
                checkIsValidateDataPassport(passport)
                passportList.append(passport)
                passport = Passport()

            passport.completePassport(line)          
    
    return passportList

# Check only if exist a value in the requered fields from a passport.           
def checkIsValidatePassport(passport):
    if(passport != None and type(passport) == Passport and 
            passport.byr != '' and 
            passport.iyr != '' and 
            passport.eyr != '' and 
            passport.hgt != '' and 
            passport.hcl != '' and 
            passport.ecl != '' and 
            passport.pid != ''):
        passport.isValidPassport = True

# Check if exist a value in the requered fields from a passport and the data integration.
def checkIsValidateDataPassport(passport):

    if(passport != None and 
            type(passport) == Passport and 
            passport.byr != '' and checkIsFourDigitInRange(passport.byr,1920,2002) and
            passport.iyr != '' and checkIsFourDigitInRange(passport.iyr,2010,2020) and
            passport.eyr != '' and checkIsFourDigitInRange(passport.eyr,2020,2030) and
            passport.hgt != '' and checkHeight(passport.hgt) and
            passport.hcl != '' and re.match("^#[A-Fa-f0-9]{6}$", passport.hcl) != None and
            passport.ecl != '' and re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport.ecl) != None and
            passport.pid != '' and re.match("^[0-9]{9}$", passport.pid) != None):
        passport.isValidDataPassport = True

# Check if a string is a number of four digit in the range.
def checkIsFourDigitInRange(value, minValue, maxValue):
    try:
        return (value != None and
                len(value) == 4 and
                type(int(value)) == int and
                int(value) >= minValue and
                int(value) <= maxValue)
    except ValueError:
        return False

# Check height field like the description in the problem.
def checkHeight(value):
    isValid = False

    if(value != None and len(value) > 0):
        if (value.find("cm") != -1):
            try:               
                number = int(value.replace('cm', ''))
                isValid = (150 <= number <= 193)
            except ValueError:
                return False
        elif (value.find("in") != -1):
            try:               
                number = int(value.replace('in', '')) 
                isValid = (59 <= number <= 76)
            except ValueError:
                return False

    return isValid

# Main execution program.
if __name__ == "__main__":

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        file = readFile(sys.argv[1])
        passportList = foundAllPassport(file)

        print("There are ",sum(1 for item in passportList if item.isValidPassport == True)," valid passports")      
        print("There are ",sum(1 for item in passportList if item.isValidDataPassport == True)," valid passports with data validation")
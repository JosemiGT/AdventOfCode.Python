"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 2. 
    Problem description: https://adventofcode.com/2020/day/2
    Input: https://adventofcode.com/2020/day/2/input

    PART 1. How many passwords are valid according to their policies?
    PART 2. How many passwords are valid according to the new interpretation of the policies?
"""
# Modules needed in this script.
import sys
import os

class PassConfig(object):

    numMin = 0
    numMax = 0
    textCheck = ''
    passwordCheck = ''
    isValid = False
    isValidPosition = False

    def __init__(self, passwordLine):
        self.readPasswordLine(passwordLine)
        self.checkPassword()
        self.checkPasswordPosition()

    def readPasswordLine(self, passwordLine):
        lineSplit = passwordLine.split(': ')
        self.passwordCheck = lineSplit[-1]
        policy = lineSplit[0]
        policySplit = policy.split('-')
        self.numMin = int(policySplit[0])
        self.numMax = int(policySplit[-1].split()[0])
        self.textCheck = policySplit[-1].split()[-1]
    
    def checkPassword(self):
        countText = 0
        passSize = len(self.passwordCheck)
        textSize = len(self.textCheck)

        for count in range(0,passSize):
            if(self.passwordCheck[count:count+textSize]==self.textCheck):
                countText += 1

        if self.numMin <= countText <= self.numMax:
            self.isValid = True
    
    def checkPasswordPosition(self):
        countText = 0
        textSize = len(self.textCheck)

        if(self.passwordCheck[self.numMin-1:self.numMin-1+textSize]==self.textCheck):
            countText += 1

        if(self.passwordCheck[self.numMax-1:self.numMax-1+textSize]==self.textCheck):
            countText += 1

        if(countText == 1):
            self.isValidPosition = True
# Read a path and return a list where a line is an item.
def readFile(path):
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

# Main execution program.
if __name__ == "__main__":

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        file = readFile(sys.argv[1])

        correctPassword = []
        correctPasswordPosition = []
        for line in file:
            passw = PassConfig(line)
            if(passw.isValid):
                correctPassword.append(passw)
            if(passw.isValidPosition):
                correctPasswordPosition.append(passw)
        
        print("The number of correct password is: ", len(correctPassword))
        print("The number of correct password with position is: ", len(correctPasswordPosition))

    else:
        print("Please, the argument must be a path file.")
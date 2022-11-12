"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 6. 
    Problem description: https://adventofcode.com/2020/day/6
    Input: https://adventofcode.com/2020/day/6/input

    PART 1: For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
"""

# Modules needed in this script.
import sys
import os

# Read a path and return a list where a line is an item.
def readFile(path):
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

# Answer Person class
class AnswerPerson(object):

    def __init__(self, line):
        self.answerYes = line
        self.answerYesList = []
        self.readAnswer(line)
    
    def readAnswer(self, line):
        if(line != None and line != '' and len(line) > 0):
            for char in line:
                if char not in self.answerYesList:
                    self.answerYesList.append(char)

# Answer Group class.
class AnswerGroup(object):

    def __init__(self):
        self.differentAnswer = []
        self.numberDifferentAnswer = 0
        self.answerPersonGroup = []
        self.sameAnswer = []
        self.numberSameAnswer = 0

    def readAnswer(self, line):
        if(line != None and line != '' and len(line) > 0):

            self.answerPersonGroup.append(AnswerPerson(line))

            for char in line:
                if char not in self.differentAnswer:
                    self.differentAnswer.append(char)

    def calculateTotalNumber(self):
        self.numberDifferentAnswer = len(self.differentAnswer)

    def calculateSumSameAnswer(self):
        if(self.answerPersonGroup != None and len(self.answerPersonGroup) > 0 and self.differentAnswer != None and len(self.differentAnswer) > 0):
            self.sameAnswer = self.differentAnswer.copy()

            for answer in self.differentAnswer:
                isFound = False
                count = 0
                
                while(isFound == False and count < len(self.answerPersonGroup)):

                    if (self.answerPersonGroup[count] != None and type(self.answerPersonGroup[count]) == AnswerPerson and answer not in self.answerPersonGroup[count].answerYesList):
                        self.sameAnswer.remove(answer)
                        isFound = True

                    count += 1

    def calculateTotalNumberSameAnswer(self):
        self.numberSameAnswer = len(self.sameAnswer)

                    

# Found and complete the passport information from a text file.
def foundAllAnswerGroup(file):
    answerGroups = []

    if(file != None and len(file) > 0):

        answerGroup = AnswerGroup()

        for line in file:
            if line == '\n' or line == '':
                answerGroup.calculateTotalNumber()
                answerGroup.calculateSumSameAnswer()
                answerGroup.calculateTotalNumberSameAnswer()
                answerGroups.append(answerGroup)
                answerGroup = AnswerGroup()
            else:
                answerGroup.readAnswer(line)      
    
    return answerGroups

def sumAnswerDifferentFromGroups(answerGroups):
    sumNumber = 0

    if(answerGroups != None and len(answerGroups) > 0):
        for answerGroup in answerGroups:
            if (type(answerGroup) == AnswerGroup):
                sumNumber += answerGroup.numberDifferentAnswer
    
    return sumNumber

def sumAnswerSameFromGroups(answerGroups):
    sumNumber = 0

    if(answerGroups != None and len(answerGroups) > 0):
        for answerGroup in answerGroups:
            if (type(answerGroup) == AnswerGroup):
                sumNumber += answerGroup.numberSameAnswer
    
    return sumNumber

# Main execution program.
if __name__ == "__main__":

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        file = readFile(sys.argv[1])
        answerGroups = foundAllAnswerGroup(file)

        print("The sum of different answer in each group is: ", sumAnswerDifferentFromGroups(answerGroups))

        print("The sum of same answer in each group is: ", sumAnswerSameFromGroups(answerGroups))
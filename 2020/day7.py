"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 7. 
    Problem description: https://adventofcode.com/2020/day/7
    Input: https://adventofcode.com/2020/day/7/input

    PART 1: How many bag colors can eventually contain at least one shiny gold bag? 
"""

# Modules needed in this script.
import sys
import os

# Global contrainst.
NAME_COLOUR_BAG_TARGET = "shiny gold"

class Bag (object):

    def __init__(self, line):
        self.nameColour = ''
        self.bagsContain = []
        self.text = line
        self.deserializeLine(line)
    
    def deserializeLine(self, line):
        if(line != None and line != None and type(line) == str and len(line) > 0):
            self.nameColour = line.split(' bags contain ')[0]
            self.deserialiceContainsBag(line.split(' bags contain ')[-1])

    def deserialiceContainsBag(self, textContain):
        if(textContain != None and textContain != None and type(textContain) == str and len(textContain) > 0):
            textContain = textContain.replace('.','')
            listBags = textContain.split(', ')

            for bag in listBags:
                if (bag != None and bag != '' and len(bag) > 0):
                    quantity = bag.split()[0]
                    nameColour = bag.replace(quantity + ' ', '')

                    contain = { nameColour, quantity}
                    self.bagsContain.append(contain)

def checkIfItContainsBag(bag, targetNameColourBag):

    isContain = False

    if(bag != None and type(bag) == Bag and targetNameColourBag != None and targetNameColourBag != ''):

        count = 0

        while(isContain == False and count < len(bag.bagsContain)):

            if(bag.bagsContain[count].nameColour != None and bag.bagsContain[count].nameColour != '' and bag.bagsContain[count].nameColour == targetNameColourBag):
                isContain = True

            count += 1

    return isContain

def searchAllPossibleBag(bags, targetNameColourBag):

    candidatesBags = []

    if(bags != None and len(bags) > 0 and targetNameColourBag != None and targetNameColourBag != ''):

        for bag in bags:
            if(checkIfItContainsBag(bag, targetNameColourBag) == True):
                candidatesBags.append(bag)
    
    return candidatesBags

def deserializeFile (file):
    
    bags = []

    if (file != None and len(file)  > 0):
        for line in file:
            bags.append(Bag(line))
    
    return bags

def branchSearch(bags, targetNameColourBag):

    resultBags = []
    isEnd = False

    

    if (bags != None and len(bags) > 0 and targetNameColourBag  != None and targetNameColourBag != ''):

        resultBags.append(targetNameColourBag)

        while(isEnd == False):
            
            # TODO:Revisar como ir actualizando la lista de target y cuando terminar el bucle.

            for target in resultBags:
                currentCandidates = searchAllPossibleBag(bags, target)

            if(currentCandidates not in resultBags):
                resultBags = agregateListToList(resultBags,currentCandidates)
            else:
                isEnd = True


def agregateListToList(mainList, secondList):

    result = []

    if (mainList != None and type(mainList) == list and secondList != None and len(secondList) > 0):

        result = mainList.copy()

        for item in secondList:
            result.append(item)
    
    return result

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
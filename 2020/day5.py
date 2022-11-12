"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 5. 
    Problem description: https://adventofcode.com/2020/day/5
    Input: https://adventofcode.com/2020/day/5/input

    PART 1: As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
    PART 2: What is the ID of your seat?
"""
# Modules needed in this script.
import sys
import os
import math

# Global contrainst.
MAX_ROW_PLANE = 127
MAX_COLUMN_PLANE = 7

# Seat Code class for store seat data.
class SeatCode(object):

    rowNumber = 0
    columnNumber = 0
    seatID = 0
    code = ''

    def __init__(self, _code):
        self.code = _code

# Read a path and return a list where a line is an item.
def readFile(path):
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

# Calculate a number from a code following the problem direction.
def calculateNumberFromCode(code, maxNumber):
    rowNumber = 0
    if(code != None and code != '' and len(code) > 0):
        minNumber = 0
        maxNumber = maxNumber

        for char in code:
            if(char == 'F' or char == 'L'):
                maxNumber = math.floor((maxNumber+minNumber)/2)
            elif(char == 'B' or char == 'R'):
                minNumber = math.ceil((maxNumber+minNumber)/2)

        if minNumber == maxNumber:
            rowNumber = maxNumber      
    
    return rowNumber

# Calculate a seat ID from the row number and column number.
def calculateSeatID(rowNumber, columnNumber):
    return rowNumber*8+columnNumber

# Transform file to SeatCode class.
def foundSeatCodes(file):

    seatCodes = []

    if(file != None and len(file) > 0):
        
        for line in file:
            if line != None and line != '':
                seatcode = SeatCode(line)
                seatcode.rowNumber = calculateNumberFromCode(line[:7], MAX_ROW_PLANE)
                seatcode.columnNumber = calculateNumberFromCode(line[7:], MAX_COLUMN_PLANE)
                seatcode.seatID = calculateSeatID(seatcode.rowNumber, seatcode.columnNumber)

                seatCodes.append(seatcode)

    return seatCodes

# Return the max seat id number.
def searchMaxSeatId(seatCodes):

    maxID = 0

    if (seatCodes != None and len(seatCodes) > 0):
        for seatCode in seatCodes:
            if seatCode != None and seatCode.seatID != None and seatCode.seatID > maxID:
                maxID = seatCode.seatID
        
    return maxID

# Return the seats near to a free seat.
def searchFreeSeat(seatCodes):

    candidatesID = []

    for seatCode in seatCodes:

        isOneDiferenceLess = False
        isOneDiferenceMore = False
        count = 0

        while((isOneDiferenceLess == False or isOneDiferenceMore == False) and count < len(seatCodes)):
            
            if((seatCode.seatID+1) == seatCodes[count].seatID):
                isOneDiferenceMore = True
            
            if((seatCode.seatID-1) == seatCodes[count].seatID):
                isOneDiferenceLess = True

            count += 1

        if(isOneDiferenceLess == False or isOneDiferenceMore == False):
            candidatesID.append(seatCode.seatID)

    return candidatesID

# Main execution program.
if __name__ == "__main__":

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        file = readFile(sys.argv[1])
        seatCodes = foundSeatCodes(file)

        maxID = searchMaxSeatId(seatCodes)
        print("Seat with max ID:", maxID)

        IDsNearFree = searchFreeSeat(seatCodes)
        print("Site ID with next site free:", IDsNearFree)


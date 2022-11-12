"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 1. 
    Problem description: https://adventofcode.com/2020/day/1
    Input: https://adventofcode.com/2020/day/1/input

    PART 1. To find the two entries that sum to 2020 and then multiply those two numbers together.
    PART 2. To find the three entries that sum to 2020 and then multiply those three numbers together.
"""

# Modules needed in this script.
import sys
import os
from itertools import combinations

# Global contrainst.
GROUP_BY_NUMBER = 3
NUMBER_SUM = 2020

# Read a path and return a list where a line is an item.
def readFile(path):
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

# Calculate the combination number, group by a number that sum to a number.
def foundNumberThatSum(numbers, groupbynumber, numberSum):
    result = []
    if(numbers != None and numberSum != None):
        combinationsNumber = combinations(numbers, groupbynumber)
        for combinationNumber in combinationsNumber:
            if(sumList(combinationNumber) == numberSum):
                result.append(combinationNumber)
    return result

# Calculate the sum from a number list.        
def sumList(numbers):
    result = 0
    if(numbers != None):
        for number in numbers:
            result += int(number)
    return result           

# Calculate the multiplication from a number list.   
def multiplyList(numbers):
    result = 0
    if(numbers != None):
        result = 1
        for number in numbers:
            result *= int(number)
    return result       

# Write a number list, calcula and print its multiplication.
def writeNumberswithMult(numbers):
    if(numbers != None):
        for numberPair in numbers:
            print(numberPair, multiplyList(numberPair)) 

# Main execution program.
if __name__ == "__main__":

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        file = readFile(sys.argv[1])
        result = foundNumberThatSum(file,GROUP_BY_NUMBER,NUMBER_SUM)
        writeNumberswithMult(result)
    else:
        print("Please, the argument must be a path file.")


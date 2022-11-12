"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 3. 
    Problem description: https://adventofcode.com/2020/day/3
    Input: https://adventofcode.com/2020/day/3/input

    PART 1: Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?  
    PART 2: What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
# Modules needed in this script.
import sys
import os

class MapLineConfig(object):

    lineSize = 0
    relativeIndex = 0
    thereIsTree = False
    newLineMap = ''

    def __init__(self, mapline, lineIndex):
        self.lineSize = len(mapline)
        self.calculateRelativeIndex(lineIndex)
        self.checkTree(mapline)
        self.writeNewMap(mapline)

    def calculateRelativeIndex(self, index):
        self.relativeIndex = index

        while(self.relativeIndex >= self.lineSize):
            self.relativeIndex = self.relativeIndex - self.lineSize
    
    def checkTree(self, mapline):
        if(mapline[self.relativeIndex] == '#'):
            self.thereIsTree = True

    def writeNewMap(self, mapline):
        self.newLineMap = mapline
        if(self.thereIsTree):
            self.newLineMap = replaceAt(mapline, self.relativeIndex, 'X')
        else:
            self.newLineMap = replaceAt(mapline, self.relativeIndex, 'O')
            
# Read a path and return a list where a line is an item.
def readFile(path):
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

def replaceAt(line, idx, char):
  return line[:idx] + char + line[idx+1:] 

# Check where is there a tree, line to line.
def CheckAllTree(file, positionJumpRight, positionJumpDown):
    index = 0
    index_down = 0
    lineWithTrees = []
    while(index_down < len(file)):

        maplineconf = MapLineConfig(file[index_down],index)
        # print(maplineconf.newLineMap) # Uncomment for view line to line in the console.

        if maplineconf.thereIsTree:
            lineWithTrees.append(maplineconf)

        index = index + positionJumpRight
        index_down = index_down + positionJumpDown

    return lineWithTrees

# Main execution program.
if __name__ == "__main__":

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        file = readFile(sys.argv[1])
        lineWithTrees31 = CheckAllTree(file, 3, 1)
        print("There are", len(lineWithTrees31), "trees")

        lineWithTrees11 = CheckAllTree(file, 1, 1)
        print("There are", len(lineWithTrees11), "trees")

        lineWithTrees51 = CheckAllTree(file, 5, 1)
        print("There are", len(lineWithTrees51), "trees")

        lineWithTrees71 = CheckAllTree(file, 7, 1)
        print("There are", len(lineWithTrees71), "trees")

        lineWithTrees12 = CheckAllTree(file, 1, 2)
        print("There are", len(lineWithTrees12), "trees")

        print("Multiply together the number of trees encountered: ", len(lineWithTrees31)*len(lineWithTrees11)*len(lineWithTrees51)*len(lineWithTrees71)*len(lineWithTrees12))

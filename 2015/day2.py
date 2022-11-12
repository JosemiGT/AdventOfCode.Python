"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 1. 
    Problem description: https://adventofcode.com/2015/day/2
    Input: https://adventofcode.com/2015/day/2/input

Find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

"""
# Modules needed in this script.
from copyreg import constructor
from importlib.metadata import SelectableGroups
from subprocess import list2cmdline
import sys
import os

# Global contrainst.
SEPARATOR_DIMENSIONS : str = 'x'

# Read a path and return a list where a line is an item.
def read_file(path:str) -> list[str]:
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

class GiftPaper:

    def __init__(self, length:int, width:int, height:int) -> None:
        self.side_length_widght = length * width
        self.side_widght_height = width * height
        self.side_height_length = height * length
        self.smallest_side = min([self.side_length_widght, self.side_widght_height, self.side_height_length])
        self.area = self.calculate_required_surface_area()

    def calculate_required_surface_area(self) -> int:
        return 2*self.side_length_widght+2*self.side_widght_height+2*self.side_height_length+self.smallest_side


def parse_line_to_gift_paper(line:str) -> GiftPaper:

    dimensions_list = line.split(SEPARATOR_DIMENSIONS)

    if(len(dimensions_list) != 3):
        raise TypeError("Dimensions are incorrent")

    return GiftPaper(int(dimensions_list[0]), int(dimensions_list[1]), int(dimensions_list[2]))


def calculate_surfaces_area_dimensions_requires(file:list[str]) -> int:

    total_area = 0

    for line in file:
        current_gift_paper = parse_line_to_gift_paper(line)
        total_area += current_gift_paper.area
        
    return total_area

# Main execution program.
if __name__ == "__main__":

    if len(sys.argv) < 1 or os.path.exists(sys.argv[1]) == False:
        raise TypeError("One argument is required!")

    file = read_file(sys.argv[1])

    total_area = calculate_surfaces_area_dimensions_requires(file)
    print("Total area: " + str(total_area))
    

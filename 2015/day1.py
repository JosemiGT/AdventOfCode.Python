"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 1. 
    Problem description: https://adventofcode.com/2015/day/1
    Input: https://adventofcode.com/2020/day/1/input

Part one:
An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor. The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

Part two:
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 
The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.


"""

# Modules needed in this script.
import sys
import os
from itertools import combinations

# Global contrainst.
OPENING_PARENTHESSIS = '('
CLOSING_PARENTHESSIS = ')'
TARGET_FLOOR = -1

# Read a path and return a list where a line is an item.
def read_file(path):
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

def calculate_floor_by_parenthesis_line(line_text):

    floor_count = 0

    for char in line_text:
        if char == OPENING_PARENTHESSIS:
            floor_count += 1
        if char == CLOSING_PARENTHESSIS:
            floor_count -= 1

    return floor_count

def calculate_floor_by_parenthesis_char(char, current_floor):

    if char == OPENING_PARENTHESSIS:
        current_floor += 1
    elif char == CLOSING_PARENTHESSIS:
        current_floor -= 1

    return current_floor

def calculate_position_target_floor(file):

    current_floor = 0

    for line in file:
        for position in range(len(line)):
            current_floor = calculate_floor_by_parenthesis_char(line[position], current_floor)

            if(current_floor == TARGET_FLOOR):
                return position + 1

    return 0

# Main execution program.
if __name__ == "__main__":

    final_floor = 0
    target_position_floor = 0

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        file = read_file(sys.argv[1])

        for line in file:
            final_floor = calculate_floor_by_parenthesis_line(line)

        target_position_floor = calculate_position_target_floor(file)

    print("Final floor: " + str(final_floor))
    print("position target floor: " + str(target_position_floor))

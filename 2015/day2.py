"""
Code for resolve the problems for https://adventofcode.com
@author: JosemiGT

Day 2. 
    Problem description: https://adventofcode.com/2015/day/2
    Input: https://adventofcode.com/2015/day/2/input

Find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

    -- Part 2 --

The feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.


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
    """Read File

    Args:
        path (str): File path

    Returns:
        list[str]: Text file by line.
    """
    try:
        with open(path, "r") as file:
            return file.read().split('\n')
    except IOError:
        print("File not accessible")

class Rectangule:
    """
        Rectangule side of a a gift class.
    """
    def __init__(self,length:int, width:int) -> None:
            self.length = length
            self.width = width
            self.perimeter = length*width
            self.distance_ribbon = 2*length+2*width

class GiftPaper:
    """Gift Paper class.
    """
    def __init__(self, length:int, width:int, height:int) -> None:
        self.side_length_widght = length * width
        self.side_widght_height = width * height
        self.side_height_length = height * length
        self.smallest_side = min([self.side_length_widght, self.side_widght_height, self.side_height_length])
        self.area = self.calculate_required_surface_area()

    def calculate_required_surface_area(self) -> int:
        return 2*self.side_length_widght+2*self.side_widght_height+2*self.side_height_length+self.smallest_side

class Ribbon:
    """Ribbon of a gift class.
    """
    def __init__(self, length:int, width:int, height:int) -> None:

        self.smaller_perimeter = self.calculatesmallerperimeter([
                                                        Rectangule(length, width),
                                                        Rectangule(width, height),
                                                        Rectangule(height, length)])
        self.volume = self.calculate_volume(
                        length, 
                        width, 
                        height)

        self.ribbon_length = self.smaller_perimeter + self.volume

    def calculatesmallerperimeter(self, rectange_list:list[Rectangule]) -> int:
        """calculate smaller perimeter

        Args:
            rectange_list (list[Rectangule]): Rectangules from a gift

        Returns:
            int: Smaller perimeter
        """

        smaller_perimeter = min([rectangule.perimeter for rectangule in rectange_list])

        return [rectangule.distance_ribbon for rectangule in rectange_list if rectangule.perimeter == smaller_perimeter][0]

    def calculate_volume(self, 
                        length:int, 
                        width:int, 
                        height:int) -> int:
        """calculate_volume

        Args:
            length (int): length
            width (int): width
            height (int): height

        Returns:
            int: volume
        """
        return length*width*height


def parse_line_to_gift_paper(line:str) -> GiftPaper:
    """Parse a line from a text file to a Gift Paper class.

    Args:
        line (str): text line

    Raises:
        TypeError: Dimensions are incorrent

    Returns:
        GiftPaper: Gift Paper instance.
    """
    dimensions_list = line.split(SEPARATOR_DIMENSIONS)

    if(len(dimensions_list) != 3):
        raise TypeError("Dimensions are incorrent")

    return GiftPaper(int(dimensions_list[0]), int(dimensions_list[1]), int(dimensions_list[2]))


def parse_line_to_ribbon(line:str) -> Ribbon:
    """Parse a line from a text file to a Ribbon class.

    Args:
        line (str): text line

    Raises:
        TypeError: Dimensions are incorrent

    Returns:
        GiftPaper: Gift Paper instance.
    """
    dimensions_list = line.split(SEPARATOR_DIMENSIONS)

    if(len(dimensions_list) != 3):
        raise TypeError("Dimensions are incorrent")

    return Ribbon(int(dimensions_list[0]), int(dimensions_list[1]), int(dimensions_list[2]))


def calculate_surfaces_area_dimensions_requires(file:list[str]) -> int:
    """Calculate surfaces area dimensions requires by the elves

    Args:
        file (list[str]): lines text from a file.

    Returns:
        int: total area
    """
    total_area = 0

    for line in file:
        current_gift_paper = parse_line_to_gift_paper(line)
        total_area += current_gift_paper.area
        
    return total_area

def calculate_ribbon_length_requires(file:list[str]) -> int:
    """Calculate ribbon requires by the elves

    Args:
        file (list[str]): lines text from a file.

    Returns:
        int: ribbon length.
    """
    total_ribbon_length = 0

    for line in file:
        current_ribbon_length = parse_line_to_ribbon(line)
        total_ribbon_length += current_ribbon_length.ribbon_length
        
    return total_ribbon_length

if __name__ == "__main__":
    """Main execution program.

    Raises:
        TypeError: One argument is required.
    """
    if len(sys.argv) < 1 or os.path.exists(sys.argv[1]) == False:
        raise TypeError("One argument is required!")

    file = read_file(sys.argv[1])

    total_area = calculate_surfaces_area_dimensions_requires(file)
    total_ribbon_length = calculate_ribbon_length_requires(file)

    print("Total area: " + str(total_area))
    print("Total ribbon: " + str(total_ribbon_length))
    

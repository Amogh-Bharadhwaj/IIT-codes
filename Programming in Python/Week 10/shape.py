'''A class named Shape is given to you as a part of the prefix code. Write a class named Square that is derived from Shape with the following specification:

Attributes

Only those attributes that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.

side: int, side of the square
Methods

Only those methods that are specific to the derived class are mentioned below. The rest have to be inherited from the base class.

__init__: accept side as an argument:
	Call the constructor of the base class and set the name attribute to "Square" using it.
	Assign side to the corresponding attribute of this class.
	Call the methods compute_area and compute_perimeter within the constructor.
compute_area: compute the area of the square and assign it to the attribute area.
compute_perimeter: compute the perimeter of the square and assign it to the attribute perimeter.'''

#NOTE DOES NOT WORK

class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')
class Square(Shape):
    def compute_area(self,side):
        self.area = side * side
    def compute_perimeter(self,side):
        self.perimeter = 4 * side
    def __init__(self, side):
        #super().__init__(name)
        self.side = side
        compute_area(self.side)
        compute_perimeter(self.side)
'''Create a class triangle that accepts 3 side lengths as input.
It should have the following methods:
    is_valid():
        returns valid if triangle is valid else invalid
    side_classification():
        return invalid if invalid else equilateral, isoceles or scalene
    angle_classification():
        return invialid else acute, right, obese
    area():
        return invalid else area'''
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def is_valid(self):
        if self.a+self.b >self.c and self.a+self.c >self.b and self.b+self.c >self.a:
            return "Valid"
        else:
            return "Invalid"
    def Side_Classification(self):
        if self.is_valid() == "Invalid":
            return "Invalid"
        elif self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles"
        else:
            return "Scalene"
    def Angle_Classification(self):
        if self.is_valid() == "Invalid":
            return "Invalid"     
        elif self.a**2 + self.b**2 > self.c**2:
            return "Acute"
        elif self.a**2 + self.b**2 == self.c**2:
            return "Right"
        else:
            return "Obtuse"
    def Area(self):
        if self.is_valid() == "Invalid":
            return "Invalid" 
        else:
            s = (self.a + self.b + self.c)/2
            return (s * (s-self.a) * (s - self.b) * (s-self.c))**0.5        
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())

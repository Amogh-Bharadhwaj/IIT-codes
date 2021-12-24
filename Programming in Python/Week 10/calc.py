'''Create a class named Calculator that has the following specification:

Attributes

a: int, we shall call this the first attribute

b: int, we shall call this the second attribute

Methods

__init__: accept two arguments a and b, assign them to the corresponding attributes

add: return the sum of the two attributes

multiply: return the product of the two attributes
subtract: subtract the second attribute from the first and return this value
quotient: return the quotient when the first attribute is divided by the second attribute
remainder: return the remainder when the first attribute is divided by the second'''

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def quotient(self):
        return self.a // self.b
    def remainder(self):
        return self.a % self.b
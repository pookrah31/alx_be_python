import math

class Shape:
    def area(self):
        raise NotImplementedError("Derived classes need to override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__ (self, radius):  
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
       

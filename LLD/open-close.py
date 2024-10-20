# SOLID
# O : Open/Closed Principle

"""Software entities(classes, modules, functions, etc.) should be open for extension and always 
close for modification

: This means that the design of software should be such that you can introduce new functionality or
behavior without modifying  the existing code since changing the existing code might introduce bugs
"""

# Code example 
"""
Let's say you have a ShapeCalculator class that calculates the area and
perimeter of different shapes like rectangles and circles.
"""

class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius ** 2)

    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape.type == "circle":
            return 3.14 * shape.radius * 2


# here if we want to add triangle then we have to modify the calculate_area function and calculate_permeter
# It will violate OCP

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_area(self):
        return self.length * self.breadth
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

# Now we can extend this method without changing the actual function
# let say now we need to add triangle, square

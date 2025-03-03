"""
Inheritance is a mechanism that allows a class to inherit properties and methods from another class,
called the superclass or parent class.
"""

class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def honk(self):
        print("Honk Honk!!")
    
class Car(Vehicle):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed
        

    def accelerate(self):
        self.speed += 10


my_car = Car("red", 30)
my_car.honk()
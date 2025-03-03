"""
A class is a blueprint or template that defines the properties and behavior of an object.
An Object is an instances of a class, created using the class definition.
"""

class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
    
    
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is starting.")


toyota_car = Car("Toyota", "Camry", 2020)
toyota_car.start_engine()

        
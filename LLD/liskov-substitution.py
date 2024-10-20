# SOLID
# L: Liskov Substitution Principle

"""Objects of a superclass  should be replaceable with objects of its subclass 
without affecting the correctness of the program
"""

# Code Example:
"""Let's consider a scenario where we have a base class Vehicle and two derived classes Car and Bicycle.

Without following the LSP, the code might look like this:
"""

class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Bicycle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Bycycle does not have engine")


"""In this example the Bicycle class violates the LSP because it provides  an implementation for the
start_engine method, which doesn't make sense for bicycle
"""
# TO fix this we have to make it generalized

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        return "Starting the car engine"

class Bicycle(Vehicle):
    def start(self):
        return "Pedaling the bicycle"


    
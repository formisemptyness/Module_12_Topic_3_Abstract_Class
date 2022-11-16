'''
Program: abstract_class.py
Author: Joshua M. McGinley
Last date modified: 11/16/2022


Write an abstract class Rider with ride and riders abstract methods. Write subclasses Bicycle, Motorcycle,
Car that implement (override) the abstract methods.

Include your driver code. Create on object of each Bicycle, Motorcycle and Car. Call the methods for each.

Sample output could include:

Human powered, not enclosed
1 or 2 if tandem or a daredevil

Engine powered, not enclosed
1 or 2

Engine powered, enclosed
1 plus comfortably
'''

from abc import ABC, abstractmethod

class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass

    def riders(self):
        pass

class Bicycle(Rider):

    def __init__(self):
        self.ride = 'Human powered, not enclosed'
        self.riders = '1 or 2 if tandem or a daredevil'

    def ride(self):
        print(str(self.ride))

    def riders(self):
        print(str(self.riders))

    def __str__(self):
        return str(self.ride) + "\n" + str(self.riders)

class Motorcycle(Rider):

    def __init__(self):
        self.ride = 'Engine powered, not enclosed'
        self.riders = '1 or 2'

    def ride(self):
        print(str(self.ride))

    def riders(self):
        print(str(self.riders))

    def __str__(self):
        return str(self.ride) + "\n" + str(self.riders)

class Car(Rider):

    def __init__(self):
        self.ride = 'Engine powered, enclosed'
        self.riders = '1 plus comfortably'


    def ride(self):
        print(str(self.ride))

    def riders(self):
        print(str(self.riders))

    def __str__(self):
        return str(self.ride) + "\n" + str(self.riders)


m = Motorcycle()
b = Bicycle()
c = Car()
print(str(b))
print('\n')
print(str(m))
print('\n')
print(c)

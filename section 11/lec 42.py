
polymorphism:

class Animal :
    def speak(self):
        return "sound of speaking"
    

class Dog(Animal):
    def speak(self):
        return "dog barks"
    

class Cat(Animal):
    def speak(self):
        return "cat meows"
    
dog1=Dog()
print(dog1.speak())

cat1=Cat()
print(cat1.speak())

o/p -> dog barks
    cat meows


#polymorphism with absract base class 
from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def self_engine(self):
        pass

class Car(Vehicle): #derived class 1
    def self_engine(self):
        return " car engine started"
    
class Motorcycle(Vehicle): #derived class 2
    def self_engine(self):
        return " motorcycle engine started"
    
def start_driving(vehicle): #function that demonstrate polymorphism
    print(vehicle.self_engine())

#car is object of CAR

car=Car()
start_driving(car)

o/p = car engine started


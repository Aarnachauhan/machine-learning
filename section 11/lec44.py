abstract method

from abc import ABC , abstractmethod
class Vehicle(ABC):
    def drive(self):
        print("driver is about to drive")
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
        def start_engine(self):
            print("car engine started")


        def operate(vehicle):
          vehicle.start_engine()
          vehicle.drive()

        car=Car()
        operate(car)


o/p-
car engine started
drier is about to drive

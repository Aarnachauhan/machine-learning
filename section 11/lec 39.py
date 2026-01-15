class Dog:
  #constructor
    def __init__ (self, name,age):
        self.name=name #name and age are instance variable
        self.age=age
#creating object:
dog1=Dog("buddy",4)
print(dog1)


#calling with instance method
class Dog:
    def __init__ (self, name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(f"{self.name} says woof")

dog1=Dog("buddy",4)
dog1.bark()

o/p -> buddy says woof


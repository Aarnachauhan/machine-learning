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
--------------------------------------------------------------------------------------------------------------
class Account:
    def __init__ (self , owner , balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is the amount deposited")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            balance-=balance

    
    
acc=Account("aarna",5000)
print(acc.balance)

acc.deposit(100)

print(acc.balance)



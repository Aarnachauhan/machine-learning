magic methods
 ##init 
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

person=Person("aarna",21)
print(person)
o/p- <__main__.Person object at 0x0000021CD483E900>

##str
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}, is  {self.age} years old"

person=Person("aarna",21)
print(person)
o/p-aarna, is  21 years old



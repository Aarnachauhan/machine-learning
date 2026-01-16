encapsulation

#public variables
class Person():
    def __init__(self,name,age):
        self.name=name #public variables
        self.age=age  #public variables

def get_name(person):
    print(person.name)

person=Person("aarna",21)
get_name(person)


#private
class Person():
    def __init__(self,name,age,gender):
        self.__name=name #name and age is private v
        self.__age=age
        self.gender=gender # public v

def get_name(person):
    return person.__name

def get_gen(person):

    return person.gender

person=Person("aarna",21,"female")
get_gen(person)

here gender is public so we can access it, otherwise we cant access it like name and age .
  if we run dir(person)
  we will see gender but name as _Person__name and same as age


#protected
class Person():
  def __init__(self,name,age,gender):
        self._name=name #name and age is protected v
        self._age=age
        self.gender=gender # public v

class Employee(Person):
    def __init(self,name,age,gender):
        super().__init__(name,age,gender)
person=Employee("aarna",21,"female")
print(person._name)


we cant use it outside class but we can use it in derived class


#encapsulation with getter and setter 
class Person():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name
        return self.__name

person=Person("aarna",20)
print(person.get_name())
print(person.set_name("krish"))


o/p-
aarna
krish



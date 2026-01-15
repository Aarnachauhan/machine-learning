
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

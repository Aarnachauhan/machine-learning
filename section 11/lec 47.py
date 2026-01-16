
class Vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self , other):
        return Vector(self.x + other.x , self.y + other.y)
    
    def __sub__(self,other):
        return Vector(self.x - other.x , self.y-other.y)
    
    def __mul__(self,other):
        return Vector(self.x*other.x , self.y*other.y)
    
    def __truediv__(self,other):
        return Vector(self.x / other.x , self.y / other.y)
    
    def __eq__(self,other):
        return Vector(self.x / other.x , self.y / other.y)
    
    def __repr__(self):
        return f"Vector ({self.x},{self.y})"
    
v1=Vector(5,5)
v2=Vector(4,2)
  
print(v1+v2)
print(v1*3)

o/p - Vector(9,7)
Vector(6,9)


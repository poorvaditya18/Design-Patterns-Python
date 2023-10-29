import math
# example of operator overloading --
class Vector:

    def  __init__(self, x, y):
        self.x = x
        self.y = y
    
    # operator overloading 
    # note : "other" should be of the same type  , it should also have same attributes else it will throw error. 
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    
    # how you represent your class 
    # --> str means this will return a string
    def __repr__(self)->str:
        return f"{self.x}i + {self.y}j"

    def magnitude(self)->float:
        return math.sqrt(self.x*self.x + self.y*self.y)

# creating 2 vectors
v1 = Vector(10,20)
v2 = Vector(10,30)

print(v1)
print(v2)

# now we want to add these two vectors 
v3 = v1 + v2  # think like this -->  v1.add(v2) then storing these result in another vector v3 

print("Resultant vector =" , v3)

print("length of vector v3 = ", v3.magnitude())
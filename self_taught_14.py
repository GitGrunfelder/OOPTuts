# An example of how to create a class variable outside of the init and other methods.
class Rectangle():
    dimensions_of_rectangles = []
    
    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.dimensions_of_rectangles.append((self.width, self.length))
    
    def print_size(self):
        print(f"{self.width} by {self.length}")

r1 = Rectangle(5, 4)
r2 = Rectangle(6, 8)
r3 = Rectangle(10, 8)

print(Rectangle.dimensions_of_rectangles)


# In this instance, the Lion class inherits the __repr__ magic method from the Object class. (All classes inherit from the Object class.)
# __repr__ is called to 'represent' the object as a string and allow for printing.
# These magic methods can be overwritten. 
class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Tom")
print (lion)

# Here is an example of overwriting the magic method to allow printing of the name string.
class Lion:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name

lion = Lion("Tom")
print (lion)


# When the '+' operator is used, the first object is put into __add__, and the second object is put into __add__ as a parameter.
# Here, the abs function is used to return the absolute value of any two objects passed in.
# The result will always be positive.
class AlwaysPositive:
    def __init__(self, number):
        self.n = number
        
    def __add__(self, other):
        return abs(self.n + other.n)
    
x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

# Use 'is' keyword to see if something is the same. Since same_bob and bob point to same variable, this is true.
# Since another_bob is a new person object, it is false.
class Person:
    def __init__(self):
        self.name = "Bob"
        
bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

x = 10
if x is None:
    print("x is None")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None")
else:
    print("x is not None")

#______________________CHALLENGES_______________________________
class Square:
    square_list=[]
    
    def __init__(self, l):
        self.length = l
        self.sides = f"{l} by {l} by {l} by {l}"
        Square.square_list.append(self.length)
    
    def __repr__(self):
        return self.sides 

sq1 = Square(10)
sq2 = Square(5)
sq3 = Square(6)

print(sq2)
print(sq1 is sq1)
print(sq1 is sq2)

def same_check(obj1, obj2):
    if obj1 is obj2:
        print("These are the same!")
    else:
        print("These are not the same!")
        
same_check(sq1, sq1)
same_check(sq2, sq1)













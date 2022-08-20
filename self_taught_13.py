# Encapsulation

class Rectangle:
    # These variable represent the state
    def __init__(self, l , w):
        self.length = l
        self.width = w
    
    # Created a method using parameters from object it-'self' , can call method.
    def area(self):
        return self.width * self.length
    

rectangle1 = Rectangle(10, 20)
print(rectangle1.area())

# Encapsulation also refers to hiding data from users. 
class Data:
    # These variable represent the state
    def __init__(self):
        self.numbers = [5, 10, 20]
        # This naming convention, with an underscore in front of var, denotes private variable. Not safe to change.
        self._priv_data = (0, 1, 2)
    
    # Can change the data use a method.
    def change_number(self, index, n):
        self.numbers[index] = n
    
    # This is an example of a private method, an unsafe method.
    def _change_data(self):
        self._priv_data[0] = 100
    

data1 = Data()
print(data1.numbers)
data1.change_number(0,100)
print(data1.numbers)
data1._change_data() #<--- Throws error, shouldn't have invoked method on a tuple, denoted by naming with underscore.

#-----------------------------INHERETANCE----------------------------
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    
    def print_size(self):
        print(f"{self.width} by {self.length}")
        
my_shape = Shape(10, 20)
my_shape.print_size()

# Here, you can create a new class as a child class, pass it the parent class
# and it inherits the parents attributes. It gains length/width, and ability to print.
# This class can overwrite methods by creating methods with same names as parent.
class Square(Shape):
    pass


my_square = Square(5, 4)
my_square.print_size()

#___________COMPOSITION____________________

# You can store an object as a variable in another object, think of it as "has a" relationship
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

cat = Person("Catherine Evans")
dog1 = Dog("Zena", "Pitbull", cat) # <-- dog1 has an owner, which is a Person Object 'cat' named "Catherine Evans"
print(dog1.name, dog1.breed, dog1.owner.name)

# ____________________________CHALLENGES_______________________________
class Shape:
    def __init__(self):
        pass
    
    def what_am_i(self):
        print("I am a shape.")
        
        
class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
    
class Square(Shape):
    def __init__(self, l):
        self.length = l
        
    def calculate_perimeter(self):
        return (self.length * 4)
    
    def change_size(self, adjustment):
        if (self.length) + adjustment > 0:
            return (self.length + adjustment) * 4
        else:
            print("Value must not reduce length to zero or lower.")
            

class Horse:
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider
        

class Rider:
    def __init__(self, name):
        self.name = name
        

rectangle1 = Rectangle(10, 20)
square1 = Square(10)
print(rectangle1.calculate_perimeter())
print(square1.calculate_perimeter())

print(square1.change_size(-9))

rectangle1.what_am_i()
square1.what_am_i()

cat = Rider("Catherine!")
my_horse = Horse("Tom", "Brown", cat)
print(my_horse.rider.name)


        
        

        
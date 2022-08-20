import math


class Person:
    # Always name the first parameter of a method 'self' 
    # When you call a method on an object, the object is automatically
    # passed to the method as a parameter.
    def __init__(self, h, w): # Initialize function (magic method)
        self.height = h
        self.weight = w
        print("Created!")
    
    def income(self, h, p):
        self.paycheck = h * p
        
        
class Rectangle:
    
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def area(self):
        return self.width * self.length
    
    def change_size(self, l, w):
        self.length = l
        self.width = w


class Apple:
    
    def __init__(self, type, color, weight, price):
        self.type = type
        self.color = color
        self.price = price
        self.weight = weight


class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
    
    def area_of_circle(self):
        return math.pi * (self.radius ** 2)


class Triangle:
    
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def triangle_area(self):
        return (self.length * self.width) / 2
    
    
class Hexagon:
    
    def __init__(self,l):
        self.length = l
        
    def perimeter(self):
        return self.length * 6
        
        
# This object has a type of Person!
george = Person("5' 11\"", 140)
# You can edit an instance variable outside of the class.
george.weight = 145
print(george.weight)
print(george.height)
# You can call a method, give parameters, and it will assign the value to an instance variable. 
george.income(80, 17)
print(george.paycheck)

box = Rectangle(10,20)
print(box.area())
box.change_size(30,5)
print(box.area())

snack = Apple("Fuji", "Red", "10 oz", "$1.00")
print(snack.type)

circle = Circle(5)
print(circle.diameter)
print(circle.area_of_circle())

triangle = Triangle(10,20)
print(triangle.triangle_area())

hexagon = Hexagon(25)
print(hexagon.perimeter())
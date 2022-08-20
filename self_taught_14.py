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


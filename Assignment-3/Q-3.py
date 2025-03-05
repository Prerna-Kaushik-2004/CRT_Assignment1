class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius   
    def area(self):
        return 3.14 * self.radius * self.radius  
a=Rectangle(10,20)
b=Circle(5)
print(f"Area of Rectangle: {a.area()}")
print(f"Area of Circle: {b.area()}")       
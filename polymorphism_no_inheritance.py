class Shape:

    def __init__(self):
        self.sides = 0


class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height

class Circle:  # derived form Shape class
    # initializer
    def __init__(self, radius):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)

class Calculations:

    def calculate_area(self, shape):
        return shape.getArea()


calculation = Calculations()
rect = Rectangle(5,4)
circ = Circle(5)

print('Area of rectangle:', calculation.calculate_area(rect))         # terminal output: Area of rectangle: 20
print('Area of circle:', calculation.calculate_area(circ))            # terminal output: Area of circle: 78.55
class Shape:

    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height

class Circle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, radius):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


rect = Rectangle(5,4)
circ = Circle(5)

print('Area of rectangle:', rect.getArea())         # terminal output: Area of rectangle: 20
print('Area of circle:', circ.getArea())            # terminal output: Area of circle: 78.55

        
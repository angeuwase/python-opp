class Circle:
    # Insert your code here
    def __init__(self, radius):
        self.radius =  radius
    
    def print_area(self):
        return 3.14 * (self.radius)**2

circle1 = Circle(3)

print(circle1.print_area())
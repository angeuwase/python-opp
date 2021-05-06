class Vehicle:
    fuelCap = 50
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model

    def printDetails(self):
        print('Color:', self.color)
        print('Make:', self.make)
        print('Model:', self.model)

    def display(self):
        print('I am from the Vehicle class')

class Car(Vehicle):
    fuelCap = 80

    def __init__(self, color, make, model, doors):
        super().__init__(color, make, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print('Doors:', self.doors)
    
    def display(self):
        super().display()
        print('I am from the Car class')
        print("Fuel cap from the Vehicle Class:", super().fuelCap)
        print("Fuel cap from the Car Class:", self.fuelCap)

car1 = Car('Silver', 'Mazda', 2015, 4)
car1.printCarDetails()
car1.display()                                          

# Terminal output:
# Color: Silver
# Make: Mazda
# Model: 2015
# Doors: 4
# I am from the Vehicle class
# I am from the Car class
# Fuel cap from the Vehicle Class: 50
# Fuel cap from the Car Class: 80

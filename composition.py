# perform composition between a sedan car class and its engine!
# implement a Sedan class, which inherits from the Car class and contains a SedanEngine object.
# Car initializer should take arguments in the order Car(model,color).
# Car class should have two properties:
# model
# color
# Car class should have one method:
# printDetails(), which will print model and color of the Car object.
# SedanEngine class will have two methods:
# start(), which will print:
# Car has started.
# stop(), which will print:
# Car has stopped.
# Sedan initializer should take arguments in the order Sedan(model, color).
# Sedan class will have one property:
# engine, which is a SedanEngine class object that should be created when the object is initialized.
# Sedan class will have two methods:
# setStart(), which will call the start() method of SedanEngine.
# setStop(), which will call the stop() method of SedanEngine.

class Car:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    def printDetails(self):
        print('Color:', self.color)
        print('Model:', self.model)

class SedanEngine:
    def start(self):
        print('Car has started.')

    def stop(self):
        print('Car has stopped.')

class Sedan(Car):

    def __init__(self, color, model):
        super().__init__(color, model)
        self.engine = SedanEngine()

    def setStart(self):
        self.engine.start()

    def setStop(self):
        self.engine.stop()


car1 = Sedan("Toyota","Grey")
car1.setStart()
car1.printDetails()
car1.setStop()

# Terminal output:
# Car has started.
# Color: Toyota
# Model: Grey
# Car has stopped.
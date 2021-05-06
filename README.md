# python-opp
Object Orientated Programming

## OOP
-Python is a multiparadigm programming language. One of the programming paradigms (way of solving problems) it supports is object orientated programming.  
-In OOP, a problem is solved by dividing it into smaller components (classes) and creating objects of those classes that interact with each other.  
-OOP allows us to create user-defined data types   
-Since the class is sharable, the code can be reused.  


## Classes and objects 
A class is a blueprint for creating objects.   
When you define a class you are giving python a description of the objects of the class. No objects are actually created, so no memory or storage is allocated.   

An instance is a specific object created from a particular class. An object is a collection of data (attributes) and code (methods) encapsulated in a single unit.  
-The attributes and methods are accessed using dot notation.   
```
object.attribute
object.method()

```
*Attributes are variables that contain information about specific properties that define the object (ie data) eg id, name, height.  
There are 2 types of attributes: class attributes and instance attributes.  

Class attributes are defined in the body of the class and are the same for all objects of the class. A change in the class variable will change the value of that property in all the objects of the class.  
-Class variables are useful when implementing properties that should be common and accessible to all class objects  
eg for Animals class : species 
For Player class: teamName, teamMembers

Instance attributes are defined in the initializer method and vary from object to object. A change in the instance variable will change the value of the property in that specific object only.  
*Methods are functions defined inside the body of a class.  
-They define specific actions that can be performed on the object (ie its behaviors).  
-Methods are called instance methods because they can only be called on instances of the class in which they were defined.  

```
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)


# access class attributes
print('blu is a', blu.species)  # terminal output: blu is a bird
print('woo is a', woo.species)  # terminal output: woo is a bird

# access instance attributes
print('blu is', blu.age, 'years old')   # terminal output: blu is 10 years old
print('woo is', woo.age, 'years old')   # terminal output: woo is 15 years old
```

## Methods 
Methods act as an interface between a program and the attributes of an object. They can be used to alter the values of the attributes or use their values to perform particular computations.  
-Methods can accept parameters and may or may not return values.   
-The first argument of any method needs to be the `self` parameter. It is only passed in the method definition and not when the method is called.  
-The self parameter provides a reference to the calling object (ie the object to which the method belongs). If the user does not mention the self as the first argument, the first parameter passed to the method will be treated as the reference to the object.  
-There are 3 types of methods: class methods, instance methods and static methods  

### Initializer Method
The initializer method `__init__` is used to define and assign values to the instance attributes when an object is instantiated.  
-It is the very first piece of code that gets run when an object is instantiated.  
-It has no return type  
-All the possible instance attributes should be defined in the initializer method.  
-If a certain instance doesnt have values for certain attributes you can define the initializer to have optional parameters.  
When the object gets instantiated, if no values are passed in for the optional attributes the object will be initialized with the default values. In that way it ensures objects always get initialised to have specific attributes.   
-Method overloading: when a method has different behavior based on the arguments passed to it. This is achieved implicitly by using optional parameters in the method definition.  
-Advantages of method overloading:  
1. saves memory  
2. increases execution speed  
3. keeps code simple and clean  
4. important for implementation of polymorphism

```
class Employee:

    def __init__(self, ID=None, salary=0, department=None):
        self.id = ID
        self.salary = salary
        self.department = department


steve = Employee()
john = Employee(5,5000, 'engineering')

print('Steve id', steve.id)                     # terminal output: Steve id None
print('Steve salary', steve.salary)             # terminal output: Steve salary 0
print('Steve department', steve.department)     # terminal output: Steve department None
print('John id', john.id)                       # terminal output: John id 5
print('John salary', john.salary)               # terminal output: John salary 5000
print('John department', john.department)       # terminal output: John department engineering
```

### Class methods   
-Class methods are used to access and modify class variables. They are accessed using the class name rather than an instance of the class (you dont need to create an object to access class methods).  
-You use the decorator `@classmethod` to declare a method as a class method. The first argument passed to the method must be the `cls` parameter which refers to the class (same concept as the `self` parameter)  
-Any reference to a class attribute is prefixed with `cls.`   

### Static methods  
-Static methods are utility functions defined inside a class. They can also be used when you don't want any inherited classes to be able to modify the parent class's method definition.   
-They don't act on the objects, and have no direct relation to the class variables or instance variables.   
-Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. The purpose of a static method is to use its parameters to produce a useful result.  
-Static methods can be accessed using the class name or the object name.  
-You use the decorator  `@staticmethod` to declare a method as a static method. Since static methods have no reference to class variables or instance variables, you dont need to pass `self` or `cls` as the first argument.  

```
class Bird:
    species = 'bird'

    @classmethod
    def getSpecies(cls):
        return cls.species

    @staticmethod
    def demoStaticMethod():
        print('I am a static method')

print('Bird class species:', Bird.getSpecies()) # terminal output: Bird class species: bird

Bird.demoStaticMethod()                         # terminal output: I am a static method

bird1 = Bird()
bird1.demoStaticMethod()                        # terminal output: I am a static method
```

Example use case for static method:  
Let’s suppose that there is a class, BodyInfo, containing information about the physical attributes of a person. We can make a static method for calculating the BMI of any given weight and height:  
```
class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))
```

### Access Modifiers
-In python, all methods and properties in a class are publicly available by default since they provide an interface for the class properties and the main code to interact with each other. This means that they can be accessed inside the class as well as outside the class.  
-If we want to suggest that a method or attribute should not be used publicly, we have to declare it as private explicitly.  
-Access modifiers are tags that are used to restrict access to parts of a class.   
-Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class. Whatever is made private is hidden from the user and other classes.  
-You make class members private by prefixing them with the double underscore `__`.    
-Trying to access private attributes in the main code will generate an attribute error saying that the object does not have that attribute `AttributeError: 'Employee' object has no attribute 'salary'`
-Public methods can access private attributes and return their values without any error.  
-Private methods will generate an attribute error if you try to access them outside the class.  
-If it is absolutely necessary to access a private property or a method from the main code, it can be accessed using the `_<ClassName>` prefix for the property or method  

```
class Employee:

    def __init__(self, ID=None, salary=0, department=None):
        self.id = ID
        self.__salary = salary
        self.department = department

    def getSalary(self):
        return self.__salary

    def __getID(self):
        return self.id


steve = Employee()
john = Employee(5,5000, 'engineering')

print('John salary', john.__salary)                     # terminal output: AttributeError: 'Employee' object has no attribute '__salary'
print('John salary', john._Employee__salary)             # terminal output: John salary 5000
print('John salary', john.getSalary())                   # terminal output: John salary 5000
print('John id', john.getID())                          # terminal output: AttributeError: 'Employee' object has no attribute 'getID'
print('John id', john._Employee__getID())                # terminal output: John id 5

```

<hr>

## Data Hiding : Encapsulation

Encapsulation is the binding of data and the methods to manipulate that data into a single unit called a class. Encapsulation is a fundamental programming technique used to achieve data hiding in OOP.  
Information hiding is the practice of hiding the inner working of a class by providing an interface through which the outside world can interact with the class without knowing its implementation details.  
This ensures that objects from different classes can interact with each other without them making unwanted changes to the original contents of the class or having unwarranted access to the class data. 

If data is not hidden, anyone will be able to access and modify the instance and class attributes directly from the main code.  

When encapsulating classes:  
1. Make all attributes in the class private  
2. Create public methods called getters and setters through which the outside world can access and maodify the private attributes. The methods are the interface used to access and or modify the attributes  
-a getter method grants read-only access to a property’s value.  eg getName  
-a setter method grants read-write access to a property's value.  eg setName  

```
class Student:

    def getName(self):
        return self.__name

    def getRollNumber(self):
        return self.__RollNumber

    def setName(self, name):
        self.__name = name

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber
```

<hr>

## Inheritance
Inheritance is a way of creating new classes from existing classes. The new class, called the child class, inherits all the public attributes and methods of the parent class and can also add its own new attributes and methods.  
-You can use inheritance whenever you come across an 'IS A' relationship.  
eg car is a vehicle; bus is a vehicle: vehicle can be the parent class; bus and car can be child classes  
-In python, whenever you create a class it is by default a subclass of the built-in python object class. This class has very few properties and methods but does provide a strong basis for Object-Oriented Programming in Python.  

Terminology  
Parent class: base class, super class  
Child class: derived class, sub class  

Benefits
1. makes code reusable  
2. simplifies code modification
3. enables extendability
4. data hiding- The base class can keep some data private so that the derived class cannot alter it.   

### Implementation  
-The name of the parent class is placed in () when defining the child class.  
-In the initializer method of the child class, you have to define all the attributes of the child class. Then you call the parent class initializer so that the child class can inherit all the public attributes of the parent class. New attributes of the child class are defined as usual.  
-In the methods of the child class, if you want to call a method from the parent class you use the `self` prefix because the child class inherits them and they become its own.   

Super Function  
-The `super()` function is used when implementing inheritance to refer to the parent class without explicitly naming it.  
It is used to make the code more manageable.  

3 main uses cases for the `super()` function:  
1. Accessing parent class attributes
2. Calling parent class methods that have the same name as child class methods 
3. Calling the initializer of the parent class
If you use the name of the parent class, you need to pass `self` as the first argument.  
```
Vehicle.__init__(self, color, make, model)
```

If you use the super function you do not need to use `self`  
```
super().__init__(color, make, model)
```

Example of inheritance:
```
class Car:
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
```

### Types of inheritance
5 main types of inheritance:  
1. single
-A child class extends a single parent class  
eg Car -> Vehicle  

2. hierarchical
-Several child clases are derived from the same parent class  
eg Car -> Vehicle; Truck -> Vehicle  

3. multiple
-A child class is derived from more than one parent class (ie child class inherits from more than 1 immediate parent)  
eg Hybrid Engine -> CombustionEngine, ElectricEngine  

4. multi-level
-A child class extends a class that is itself derived from another class  
eg Electric -> Car -> Vehicle  

5. hybrid
-A type of inheritance which is a combination of multiple and multi-level inheritance  
eg Hybrid Engine -> CombustionEngine, ElectricEngine, both of which extend Engine   

<hr>

## Polymorphism
The word polymorphism is greek for "many forms". In OOP, polymorphism refers to using a common interface (the same method) for multiple classes (data types).  
eg A shape can be circle, rectangle, square, etc. To calculate the area of each shape, you call the same method- getArea() - on objects of each class. Although its the same method, the area of each shape is calculated differently. This is polymorphism. The getArea method takes on many forms and results in different behavior depending on the object it is called on.  

Polymorphism cuts down development time. The subclasses inherit attributes and methods from the parent class, then the developer only has to alter the code in the particular portions where the responses differ while everything else remains untouched.  

### Polymorphism using methods
-You just define the method with the same name in all the classes. Although the name is the same, the implementation will differ from class to class.  
-Easy but not very efficient  

```
class Rectangle():

    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area2
    def getArea(self):
        return (self.width * self.height)


class Circle():
    # initializer
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
```

### Polymorphism using inheritance (method overriding)
-We use polymorphism when we want a base class to inherit a method for a parent class but have a different implementation for it.  
-Method overriding is the process of redefining a parent class’s method in a subclass.  
ie if a subclass provides a specific implementation of a method that had already been defined in one of its parent classes, it is known as method overriding.  
The method in the parent class is called overridden method.  
The methods in the child classes are called overriding methods.  
Method Overriding needs inheritance and there should be at least one derived class to implement it.  

Advantages of method overriding:  
1. The child class can use the implementation given in the parent class method or define its own implementation 
2. Child classes can define their own implementation of a method without changing the implementation in the parent class  
3. Child classes can have different implementations of the same method 

```
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

```

### Operator overriding 
Whenever an operator is used in Python, its corresponding method is invoked to perform its predefined function.  
For example, when the + operator is called, it invokes the special function, `__add__`, in Python, but this operator acts differently for different data types. For example, the + operator adds the numbers when it is used between two int data types and merges two strings when it used between string data types.  
Operators in python can be overloaded so that they operate in a user-defined way. If you want to be able to add complex numbers using the + operator, you would need to overload it.  


### Abstract base classes
-Abstract base classes are used to control which class objects can or cannot be instantiated. It is used with polymorphisms as follows:  
If you have a base class that has methods defined that you want child classes to inherit and define their own implementation of it, you can make the parent class an abstract base class. What this means is that its objects cant be instantiated.  
-To define a class as a base class you make it inherit from the `ABC` class from the `abc` module. Then any method in the base class that you want the child classes to inherit and implement you decorate with the `@abstractmethod` decorator. Any method that is given that decorator MUST be defined in the child classes.  

```
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


shape = Shape()
# this will code will not compile since Shape has abstract methods without
# method definitions in it
```

<hr>

## Object Relationships
Inheritance represents a relationship between classes. You also get situations where there is a relationship between objects ie objects from different classes have to interact with each other.   

There are 3 main types of class relationships:  
* Inheritance: IS A  
* Association: PART-OF and HAS-A  

-Association is the most basic way to relate classes without inheritance.  
-When we say that two objects are in an association relationship, this is a generic statement which means that we don’t worry about the lifetime dependency between the objectsWhen we say that two objects are in an association relationship, this is a generic statement which means that we don’t worry about the lifetime dependency between the objects  


### Aggregation
-Follows a HAS-A model  
-Class A and class B have a has-a relationship if one or both need the other’s object to perform an operation, but both class objects can exist independently of each other. (neither is instantiated inside the other)  
-With a has-a relationship, a class has-a reference to an object of the other class. This creates a parent-child relationship between two classes, with one class owning the object of another. However, the owner object simply points to the the owned object but does not decide the lifetime of the referenced object.   
If the owner object gets deleted the owned object will still continue to exist in the pgrogram.  
-The child can only associate with one owner object  
-You need object references to implement aggregation. ie the owned object is passed as an argument to the initializer when instantiating the owner object.  

Example:  people and their country of origin. Each person is associated with a country, but the country can exist without that person  
```
class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()


c = Country("Wales", 1500)
p = Person("Joe", c)
p.printDetails()

# deletes the object p
del p
print("")
c.printDetails()
```

### Composition
-Follows a PART-OF model  
-In a PART-OF relationship, one class object is a component of another class object: Given two classes, class A and class B, they are in a part-of relation if a class A object is a part of class B object, or vice-versa.  
-The class which creates the object of the other class is known as the owner and is responsible for the lifetime of that object. In composition, the lifetime of the owned object depends on the lifetime of the owner.  
-To achieve a part-of relationship the owned objects get instantiated inside the owner object.  
-Although the classes have their own implementation, an instance of the component class can only be created once the main class object has been created. Hence, part-of is a dependent relationship.  

Example: A car is composed of an engine, tires, and doors. In this case, a Car owned these objects, so a Car is an Owner class and tires, doors, and engine classes are Owned classes.  

```
class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)


class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)


class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)


class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car color:", self.color)


car = Car(1600, 4, 2, "Grey")
car.printDetails()

```







class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def talk(self):
        return '{} says squawk'.format(self.name)

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)


# access class attributes
print('blu is a', blu.species)  # terminal output: blu is a bird
print('woo is a', woo.species)  # terminal output: woo is a bird

# access instance attributes
print('blu is', blu.age, 'years old')   # terminal output: blu is 10 years old
print('woo is', woo.age, 'years old')   # terminal output: woo is 15 years old

# access instance method
print('blu talks:', blu.talk())  # terminal output: blu talks: Blu says squawk
print('woo talks:', woo.talk())  # terminal output: woo talks: Woo says squawk


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

# implement a student class according to the rules of encapsulation
# Implement the following properties as private: name, RollNumber
# Note: Do not use initializers to initialize the properties. Use the set methods to do so. If the setter is not defined properly, the corresponding getter will also generate an error even if the getter is defined properly.


class Student:

    def getName(self):
        return self.__name

    def getRollNumber(self):
        return self.__RollNumber

    def setName(self, name):
        self.__name = name

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber

demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())
# Implement a class Student that has four properties and two methods. All these attributes (properties and methods) should be public.
# Implement a constructor to initialize the values of four properties: name, phy, chem and, bio.
# Implement a method, totalObtained, in the Student class that calculates total marks of a student.
# Using the totalObtained method, implement another method, Percentage, in the Student class that calculates the percentage of students marks. Assume that the total marks of each subject are 100. So, the combined marks of three subjects are 300.


class Student:

    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def Percentage(self):
        return (self.totalObtained()/300)*100




student1 = Student('Mark', 80, 90, 40)

print(student1.totalObtained())
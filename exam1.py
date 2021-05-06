class Student:
    # defining the properties   
    ID = None
    GPA = None

# creating an object of the Student class
Peter = Student()

# assigning values to properties of Peter
Peter.ID = 3789
Peter.GPA = 3.5

# create a new attribute for Peter
Peter.department = "Computer Science"


# Create another Student object
John = Student()
John.ID = 3790
John.GPA = 3.7


# Printing properties of Peter
print("ID =", Peter.ID)
print("GPA", Peter.GPA)
print("Department:", Peter.department)

# Printing properties of John
print("ID =", John.ID)
print("GPA", John.GPA)
print("Department:", John.department) # This will throw an error. The new property 'department' was assigned to Peter and is not accessible to any other object of the Student class, therefore John can not access it.
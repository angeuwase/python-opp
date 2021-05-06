# implement a 'Rectangle Class Using the Concepts of Encapsulation'.
# Implement a constructor to initialize the values of two private properties: length and width.
# Implement a method, area(), in the Rectangle class that returns the product of length and width. See the formula below: Area=length×width
# Implement a method, Perimeter(), in the Rectangle class that returns two times the sum of length and width


class Rectangle:

    def __init__(self, length=None, width=None):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    
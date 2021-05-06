# Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public.
# Implement a constructor to initialize the values of three properties: x, y, and z
# Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x)**2 + (self.y)**2 + (self.z)**2  


point1 = Point(1,3,5)
print(point1.sqSum())
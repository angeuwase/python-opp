# implement an animal class and its subclasses from scratch
# A parent class named Animal.
# Inside it define:
# name
# sound
# __init__()
# Animal_details() function:
# It prints the name and sound of the Animal
# Then there are two derived classes

# Dog class
# has a property family
# has an initializer that calls the parent class initializer in it through super()
# has an overridden method named Animal_details() which prints detail of the dog.

# Sheep class
# has a property color
# has an initializer that calls the parent class initializer in it through super()
# has an overridden method named Animal_details() which prints detail of the sheep.
# The derived classes should override the Animal_details() method defined in the Animal class.

# The overridden method in Dog class should print the value of family as well as the name and sound.
# The overridden method in Sheep class should print the value of color as well as the name and sound


class Animal:

    def __init__(self, name, sound):
        self.name = name 
        self.sound = sound

    def Animal_details(self):
        print('Name:', self.name)
        print('Sound:', self.sound)

class Dog(Animal):
    
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def Animal_details(self):
        super().Animal_details()
        print('Family:', self.family)

class Sheep(Animal):
    
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        print('Color:', self.color)

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()
        
# Terminal output:
#Name: Pongo
#Sound: Woof Woof
#Family: Husky
#Name: Billy
#Sound: Baa Baa
#Color: White
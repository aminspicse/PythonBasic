# Python Classes and Objects

"""
Python Classes/Objects

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
Create a Class

To create a class, use the keyword class:
"""

# Create Class
class FirstPython:
    x = 10 # property/member variable named x

# Create object
obj = FirstPython()
print(obj.x)

"""
The __init__() Function

The examples above are classes and objects in their simplest form, 
and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object is being created:
"""
class Persion:
    def __init__(self, name, age, height, width):
        self.name = name
        self.age = age
        self.height = height
        self.width = width

    def bmi(self):
        return (self.width * self.height) / self.age

    def info(self):
        inf = self.name + " Age: {}, Height: {}, Weidth: {}"
        print(inf.format(self.age, self.height, self.width))

        print(self.name+" Age: "+ format(self.age))

pobj = Persion("Md. Al Amin",24,5.6,65)

print(pobj.name)

print(pobj.bmi())

pobj.info()
# Python Inheritance
""" 
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def echo(self):
        print(self.name)


class Student(Person):
    def stdinfo(self, id, dept):
        print(self.name, id, dept)

    def echo(self): # method overwriting 
        print(self.age)

obj = Student("Md. Al Amin", 24, 5.6)
obj.echo()
obj.stdinfo("12","cse")

obj1 = Person("Amin",24,5.6)
obj1.echo()
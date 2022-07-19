
#print('Hello world')
# python single line comment

"""
python multiple line comment

"""

# python variable name are case sensetive
x = 10
X = 10.5
z = "Hello world"

print(x, X, z)

print(type(x))

# multiple variable 
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Bannana", "Mango", "Orange"
print(x, y, z)

# you can assign the same value to multiple variables in one line:
x=y=z="Orange"
print(x, y, z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
color = ["Black", "Yellow", "Orange"]
x,y,z=color
print(x, y, z)

# Global variable
# Create a variable outside of a function, and use it inside the function
x=10 #global variable
def myfun():
    a = 100 # local variable
    global b
    b = 200 # b is global variable
    print(x)
myfun()
print(b)

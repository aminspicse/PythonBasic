# Python Loops
"""
Python has two primitive loop commands:

    while loops
    for loops

"""

# While Loop
#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i<=6:
    print(i)
    i+=1

# Python For Loops
"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
language = ["Java","Python","PHP","C#"]
for x in language:
    print(x)

for x in range(5):
    print(x)

print("Range Loop")
for x in range(2,5):
    print(x)
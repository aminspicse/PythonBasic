# Python Arrays
"""
This page shows you how to use LISTS as ARRAYS, however, 
to work with arrays in Python you will have to import a library, like the NumPy library.
"""

language = ["Java","PHP","C#"]
print(language)

for x in language:
    print(x)

# Add last index
language.append("Python")
print(language)

# add to index
language[1] = "C"
print(language)

# length of array
print(len(language))

# Pop form array
language.pop(1)
print(language)

# remove from array
language.remove("Java")
print(language)

# reverse array
language.reverse()
print(language)

# Insert in array
language.insert(1,"Go")
print(language)
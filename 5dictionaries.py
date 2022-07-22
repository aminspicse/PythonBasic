
# Python Dictionaries
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:
"""
from unicodedata import name


dictionari = {
    "name": "Md. Al Amin",
    "age": "24",
    "university": "SUST"
}

print(dictionari)

# Duplicates Not Allowed
dictionari = {
    "name": "Md. Al Amin",
    "age": "24",
    "age": "20",
    "university": "SUST"
}

print(dictionari)
print(dictionari["name"])
print(dictionari.keys())

# Add Item
dictionari["height"] = "5.6 inc"
print(dictionari)

#remove
dictionari.pop("name")
print(dictionari)

# delete
del dictionari["age"]
print(dictionari)

dictionari.clear()
print(dictionari)

# LOop
dictionari = {
    "name": "Md. Al Amin",
    "age": "24",
    "age": "20",
    "university": "SUST"
}

for x in dictionari:
    print(dictionari[x])

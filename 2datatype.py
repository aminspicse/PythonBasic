"""
Python has the following data types built-in by default, in these categories:
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
"""
x = 1j # x is complex type variable by default
print(x)
# or we can declar complex type variable
x = complex(1j)
print(x)

#list
x = list(("Blue","Orange","White"))
print(x)

#tuple 
x = tuple(("Blue","Orange","White"))
print(x)

# Range
x=range(6) # or x = (0,6)
print(x)

# Maping: dict
y = dict(name= "Md. Al Amin", age=24)
print(x)
print(y)

#set
print("SET")
x = set(("apple", "banana", "cherry"))
print(x)

#frozenset
x = frozenset(("apple", "banana", "cherry"))
print(x)
# You can assign a multiline string to a variable by using three quotes:

x = """ Hello This is Md. Al Amin 
Mobile: 01689015612
Address: Taltola, Sylhet-3100 """

print(x)

# String Array
x = "Hello, World!"
print(x[5])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "Bangladesh":
  print(x)

#String Length
x = "Hello world"
print(len(x))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("best" in txt)

# Use it in an if statement:
if "free" in txt:
    print("Yes, free is present")
else:
    print("No, free is not present")

# Use it in an if statement:
if "frees" not in txt:
    print("Yes, frees is Not present")

"""
Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
x = "Hello Bangladesh,  t"
print(x[6:9])
print(x[6:])
print(x[:5])

# Upper Case
print(x.upper())
print(x.capitalize())
print(x.lower())
print(x.strip()) # remove white space
print(x.replace("H","K")) #replace H by K
print(x.split(","))

# Concate String 
a = "Hello"
b = "World"
print(a +" "+b)

# String Format
age = 24;
x = "I am Al AMin and I am {}"
print(x.format(age))
print(x.count("AMmin"))

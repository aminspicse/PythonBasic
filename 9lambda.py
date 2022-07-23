# Python Lambda
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Syntax
lambda arguments : expression
The expression is executed and the result is returned:
"""
x = lambda a: a*2
print(x(5))

# Find (a+b)2 using lambda

R = lambda a,b : a*a + 2*a*b + b*b
print(R(2,3))
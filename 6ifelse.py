
# Python Conditions and If else statements

# Find Largest number from 3 number

num1 = input("Enter Num1: ")
num2 = input("Enter Num2: ")
num3 = input("Enter Num3: ")


if num1 > num2 and num1 > num3:
    print("Num1 is Largest")
elif num2 > num1 and num2 > num3:
    print("Num2 is Largest")
else:
    print("Num3 is Largest")
import math

print("Hypotenuse calculator")
print("Enter first cathetus length in cm:")

a = int(input())

print("Enter second cathetus length in cm:")

b = int(input())

c = a**2

d = b**2

e = math.sqrt(c + d)

print(f"The length of the hypotenuse is {e}")
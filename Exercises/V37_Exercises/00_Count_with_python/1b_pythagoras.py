import math

print("Hypotenuse calculator")
print("Enter one cathetus length in cm:")

a = int(input())

print("Enter hypothenuse length in cm:")

b = int(input())

c = a**2

d = b**2

e = math.sqrt(d - c)

print(f"The length of the second cathetus is {e:.1f}")
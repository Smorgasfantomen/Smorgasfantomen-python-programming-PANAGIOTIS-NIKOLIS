import math

print("Triangle angle checker")
print("Input first angle:")

a = int(input())

print("Input second angle:")

b = int(input())

print("Input third angle:")

c = int(input())

if ((a + b + c) > 180):
    print(f"This is an impossible triangle.")
elif (a == 90 or b == 90 or c == 90):
    print(f"You have one perpendicular angle in your triangle.")
else:
    print(f"You have no perpendicular angles.")

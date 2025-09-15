import math

print("Which is the smallest number?")
print("input first number:")

a = int(input())

print("input second number:")

b = int(input())

if a > b:
    print(f"Integer {(b):.0f} is the smallest.")
elif b > a:
    print(f"Integer {(a):.0f} is the smallest.")
else:
    print(f"You've input the same numbers.")

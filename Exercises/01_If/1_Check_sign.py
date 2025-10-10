import math

print("Is the number positive or negative?")
print("input number:")

n = int(input())

if n > 0:
    print(f"The number {(n):.0f} is positive.")
elif n < 0:
    print(f"The number {(n):.0f} is negative.")
else:
    print(f"The number {(n):.0f} is zero.")

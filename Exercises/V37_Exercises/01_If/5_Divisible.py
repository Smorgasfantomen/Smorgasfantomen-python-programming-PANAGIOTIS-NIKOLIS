import math

print("Divisible")
print("Input number:")

n = int(input())

if (n % 2 == 0 and n % 5 == 0):
    print(f"The number is even and divisible by 5.")
elif (n % 2 == 0):
    print(f"The number is even.")
elif (n % 2 == 1 and n % 5 == 0):
    print(f"The number is odd but divisible by 5.")
else:
    print(f"The number is just odd.")

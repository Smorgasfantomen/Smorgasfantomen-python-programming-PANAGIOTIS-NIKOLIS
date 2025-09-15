import math

print("Luggage size")
print("Input length in cm:")

l = int(input())

if (l <= 55):
    print("Input width in cm:")
    w = int(input())
    if (w <= 40):
        print("Input height in cm:")
        h = int(input())
        if (h <= 23):
            print(f"Your luggage is acceptable.")
        else:
            print(f"Your luggage is too thick.")
    else:
        print(f"Your luggage is too wide.")
else:
    print(f"Your luggage is too long.")

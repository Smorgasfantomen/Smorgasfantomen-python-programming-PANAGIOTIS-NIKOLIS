import math

print("Medicine checker")
print("Input age:")

a = int(input())

print("Input weight:")

w = int(input())

if (3 <= a <= 7) and (w <= 40):
    print(f"Half a pill.")
elif (a >= 12 and w >= 26):
    print(f"One to two pills.")
elif (a < 3 or w < 15):
    print(f"Child is too small.")
else:
    print(f"Half to one pills.")

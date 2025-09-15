import math

print("Euclidean distance finder")
print("Enter Y-value of point one:")

Y1 = int(input())

print("Enter X-value of point one:")

X1 = int(input())

print("Enter Y-value of point two:")

Y2 = int(input())

print("Enter X-value of point two:")

X2 = int(input())

dy = Y1 - Y2
dx = X1 - X2

d = math.sqrt(dy**2 + dx**2)

print(f"The distance between point 1 & 2 is {(d):.1f} units.")
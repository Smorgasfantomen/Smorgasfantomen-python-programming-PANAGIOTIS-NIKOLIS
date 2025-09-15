import math

print("Linear equation solver")
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

K = dy / dx

m = Y1 - (K * X1)

print(f"K equals {(K):.2f}, M equals {(m):.0f}")
print(f"The equation is y = {(K)}x + {(m):.0f}")
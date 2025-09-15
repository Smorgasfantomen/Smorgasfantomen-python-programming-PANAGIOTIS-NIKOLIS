import math

print("Classification Accuracy")
print("Enter amount of samples:")

a = int(input())

print("Enter amount of correct samples:")

b = int(input())

print(f"The accuracy is {(b / a * 100):.1f}%")
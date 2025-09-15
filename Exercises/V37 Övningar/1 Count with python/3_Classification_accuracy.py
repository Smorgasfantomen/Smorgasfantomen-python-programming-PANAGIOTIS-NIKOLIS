import math

print("Classification Accuracy")
print("Enter amount of true positives:")

tp = int(input())

print("Enter amount of true negatives:")

tn = int(input())

print("Enter amount of false positives:")

fp = int(input())

print("Enter amount of false negatives:")

fn = int(input())

totalsamples = tp + tn + fp + fn

truesamples = tp + tn

print(f"The accuracy is {(truesamples / totalsamples * 100):.1f}%")
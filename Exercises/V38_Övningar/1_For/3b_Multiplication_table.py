import math

print("Pluttifikationstabellen")

print("Vilken siffras multiplikationstabell vill du se?")

i = int(input())

print("Var ska den börja?")

s = int(input())

print("Var ska den sluta?")

e = (int(input()) * i + 1)

for n in range(s, e, i):
    
    print(n, end=" ")
    n += 1


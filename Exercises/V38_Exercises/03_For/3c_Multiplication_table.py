import math

print("Pluttifikationstabellen")

f1 = 0

f2 = 0

for n in range(0, 11):
    
    for m in range(0, 11):
        print(f"{(n * m):^3}", end=" ")
        m += 1

    n += 1
    print("")


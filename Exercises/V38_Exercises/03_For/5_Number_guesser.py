import numpy
import random

print("Nummergissare")

r = random.randrange(0, 10000)


for n in range(0, 10000):
    print(n)
    print(r)
    if n == r:
        print(f"{n} was the correct guess!")
        break
    



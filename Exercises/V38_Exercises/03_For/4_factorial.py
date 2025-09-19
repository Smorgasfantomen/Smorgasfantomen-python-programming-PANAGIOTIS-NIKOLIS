import numpy

print("Vilket tal ska faktoriseras?")

i = int(input()) + 1

s = 1

for n in range(1, i):
    s *= n
    
print(s)


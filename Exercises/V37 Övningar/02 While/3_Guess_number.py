import math
import random

print("Guess number")


n = random.randrange(1, 101)
a = 1
g = 0

while g != n:

  print(f"You're on try number {a}. Guess the correct number:")
  g = int(input())
  p = n - g
  if g == n:
    print(f"Correct guess!")
    break
  elif (g < 1 or g > 100):
    print(f"You are out of span.")
  elif (-10 < (p) < 10):
    print(f"Incorrect guess, but you were quite close!")
  elif (-25 < (p) < 25):
    print(f"Incorrect guess, you were a bit off.")
  elif (-100 < (p) < 100):
    print(f"Incorrect guess, you were quite far off.")

  a += 1
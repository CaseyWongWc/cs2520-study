"""4/23 - zyBooks 11.9: Guess the random number.
Uses random.seed() for reproducibility, then randint(1,100).
"""
import random

random.seed(900)
target = random.randint(1, 100)

while True:
    g = int(input("Guess (1-100): "))
    if g < target:
        print("Too low")
    elif g > target:
        print("Too high")
    else:
        print("You got it!")
        break

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if last > 5:
    print(f"{last} and is greater than 5")
elif last == 0:
    print(f"{ast} is 0")
elif last < 6 and last != 0:
    print(f"{last} and is less than 6 and not 0")

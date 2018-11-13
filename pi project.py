import random
import math

dots_in_circle = 0
dots_in_square = 0

for i in range(1000000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if math.sqrt(x ** 2 + y ** 2) < 1:
        dots_in_circle += 1

    dots_in_square += 1

pi = (dots_in_circle / dots_in_square) * 4
print(pi)

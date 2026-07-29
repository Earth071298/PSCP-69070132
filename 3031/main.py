"""Ink"""

import math

S ,N = map(int, input().split())

for i in range(N):
    x, y = map(int, input().split())
    area = 3.1416 * (x**2 + y**2)
    time = math.ceil(area / S)

    print(time)

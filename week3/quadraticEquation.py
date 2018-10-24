#!/usr/bin/env python3

from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d == 0:
    x = -b / (2 * a)
    print(x)
elif d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
# вывод в порядке возрастания
    if x1 > x2:
        a = x1
        x1 = x2
        x2 = a
    print(x1, x2)

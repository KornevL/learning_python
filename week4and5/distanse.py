#!/usr/bin/env python3
def distance(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    ans = (x ** 2 + y ** 2) ** 0.5
    return ans
a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(distance(a, b, c, d))

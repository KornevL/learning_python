#!/usr/bin/env python3
def distance(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    ans = (x ** 2 + y ** 2) ** 0.5
    return ans


def IsPointInCircle(x, y, xc, yc, r):
    ans = distance(x, y, xc, yc) <= r
    return ans


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')

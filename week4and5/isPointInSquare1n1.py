#!/usr/bin/env python3
def IsPointInSquare(x, y):
    checkX = -1 <= x <= 1
    checkY = -1 <= y <= 1
    return checkX * checkY
x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

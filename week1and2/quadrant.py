#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
checking1 = (x1 > 0 and x2 > 0) or (x1 < 0 and x2 < 0)
checking2 = (y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0)
if checking1 and checking2:
    print('YES')
else:
    print('NO')

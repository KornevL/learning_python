#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (y1 % 2 == 0 and x1 % 2 == 0) or (y1 % 2 != 0 and x1 % 2 != 0):
    if (y2 % 2 != 0 and x2 % 2 == 0) or (y2 % 2 == 0 and x2 % 2 != 0):
        print('NO')
    else:
        print('YES')
else:
    if (y2 % 2 == 0 and x2 % 2 == 0) or (y2 % 2 != 0 and x2 % 2 != 0):
        print('NO')
    else:
        print('YES')

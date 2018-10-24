#!/usr/bin/env python3

k = int(input())
reminder = k % 3
if reminder == 0:
    print('YES')
elif k > 2 and reminder == 2:
    print('YES')
elif k > 7 and reminder == 1:
    print('YES')
else:
    print('NO')

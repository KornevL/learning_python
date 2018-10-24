#!/usr/bin/env python3

max1 = 1
n = -1
max2 = 0
n1 = int(input())
while n != 0:
    n = int(input())
    if n == n1:
        max1 += 1
    else:
        max1 = 1
    if max1 > max2:
        max2 = max1
    n1 = n
print(max2)

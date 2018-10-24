#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a < b:
    d = a
    a = b
    b = d
if a < c:
    d = a
    a = c
    c = b
    b = d
elif b < c:
    d = b
    b = c
    c = d
if a2 < b2:
    d2 = a2
    a2 = b2
    b2 = d2
if a2 < c2:
    d2 = a2
    a2 = c2
    c2 = b2
    b2 = d2
elif b2 < c2:
    d2 = b2
    b2 = c2
    c2 = d2
if a <= 0 or b <= 0 or c <= 0 or a2 <= 0 or b2 <= 0 or c2 <= 0:
    print(0)
elif a >= a2 and b >= b2 and c >= c2:
    length = a // a2
    wedth = b // b2
    height = c // c2
    sum = length * wedth * height
    print(sum)
else:
    print(0)

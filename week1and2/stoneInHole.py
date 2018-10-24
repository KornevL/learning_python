#!/usr/bin/env python3

# stone
a = int(input())
b = int(input())
c = int(input())
# hole
aHole = int(input())
bHole = int(input())
if a < b:
    d = a
    a = b
    b = d
if a < c:
    d = a
    a = c
    c = b
    b = d
if b < c:
    d = b
    b = c
    c = d
if bHole > aHole:
    s = aHole
    aHole = bHole
    bHole = s
if aHole >= b and bHole >= c:
    print('YES')
else:
    print('NO')

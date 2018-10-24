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
tghcn = a > 0 and b > 0 and c > 0
qwete = a2 > 0 and b2 > 0 and c2 > 0
if tghcn and qwete:
    if (a - a2 == 0 and b - b2 == 0) and c - c2 == 0:
        print('Boxes are equal', end='')
    elif (a - a2 <= 0 and b - b2 <= 0) and c - c2 <= 0:
        print('The first box is smaller than the second one', end='')
    elif (a - a2 >= 0 and b - b2 >= 0) and c - c2 >= 0:
        print('The first box is larger than the second one', end='')
    else:
        print('Boxes are incomparable', end='')
else:
    print('Boxes are incomparable', end='')

#!/usr/bin/env python3

# Three sides of triangle a, b, c are given.
# Determine the type of triangle with the specified sides.
# Output one of four words: rectangular for a right-angled triangle,
# acute for an acute-angled triangle,
# obtuse for an obtuse triangle
# or impossible if a triangle with such sides does not exist.
a = int(input())
b = int(input())
c = int(input())
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
h = a ** 2
k = b ** 2
l = c ** 2
if (a < b + c) and c > 0:
    if h == k + l:
        print('rectangular')
    elif h > k + l:
        print('obtuse')
    elif h < k + l:
        print('acute')
else:
    print('impossible')

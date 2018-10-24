#!/usr/bin/env python3

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
# Exchenge (c, b, a) to (a, b, c) for decreasing sequence
print(c, b, a)

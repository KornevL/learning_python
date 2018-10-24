#!/usr/bin/env python3

a = int(input())
b = int(input())
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    j = str(i)
    if j[0] == j[3] and j[1] == j[2]:
        print(j)

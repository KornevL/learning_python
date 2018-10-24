#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
k = 0
if a == b:
    k = 2
    if b == c:
        k = 3
elif b == c:
    k = 2
elif a == c:
    k = 2
print(k)

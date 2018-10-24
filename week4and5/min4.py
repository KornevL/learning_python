#!/usr/bin/env python3
def min4(a, b, c, d):
    ans = min(min(a, b), min(c, d))
    return ans
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))

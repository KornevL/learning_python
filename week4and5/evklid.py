#!/usr/bin/env python3


def gcd(a, b):
    if a * b != 0:
        a = gcd(b, a % b)
    return a


a = int(input())
b = int(input())
print(gcd(a, b))

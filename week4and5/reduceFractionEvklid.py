#!/usr/bin/env python3


def gcd(a, b):
    if a * b != 0:
        a = gcd(b, a % b)
    return a


a = int(input())
b = int(input())
n = gcd(a, b)
print(a // n, b // n)

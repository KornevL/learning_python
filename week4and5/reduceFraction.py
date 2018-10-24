#!/usr/bin/env python3


def ReduceFraction(n, m):
    i = 2
    if m % n == 0:
        m = m // n
        n = 1
    if n % m == 0:
        n = n // m
        m = 1
    while i <= n // 2:
        if n % i == 0:
            if m % i == 0:
                n, m = ReduceFraction(n // i, m // i)
        i += 1
    return n, m


n = int(input())
m = int(input())
p, q = ReduceFraction(n, m)
print(p, q)

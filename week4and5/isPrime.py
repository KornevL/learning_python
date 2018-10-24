#!/usr/bin/env python3


def IsPrime(n):
    max = int(n ** 0.5)
    i = 2
    while i <= max:
        if n % i == 0:
            return i
        i += 1
    return n


n = int(input())
if IsPrime(n) != n:
    print('NO')
else:
    print('YES')

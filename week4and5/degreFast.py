#!/usr/bin/env python3


def power(a, n):
    if n != 0:
        if n % 2 == 0:
            return a ** 2 * power(a ** 2, n // 2 - 1)
        else:
            return a * power(a, n - 1)
    else:
        return 1


a = float(input())
n = int(input())
print(power(a, n))

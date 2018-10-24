#!/usr/bin/env python3

N = int(input())
i = N
while i != 1:
    if N % i == 0:
        divisor = i
    i = i - 1
print(divisor)

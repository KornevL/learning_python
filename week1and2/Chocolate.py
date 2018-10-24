#!/usr/bin/env python3

a = int(input())
b = int(input())
k = int(input())

if (k % a == 0 or k % b == 0) and k <= a * b:
    print('YES')
else:
    print('NO')

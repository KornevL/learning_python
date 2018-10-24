#!/usr/bin/env python3
n = int(input())
for i in range(0, 4):
    for j in range(1, n + 1):
        a = ('+___', '|' + str(j) + ' /', '|__\\', '|   ')
        print(a[i], end=' ')
    print()

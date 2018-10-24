#!/usr/bin/env python3

numList = list(map(int, input().split()))
n = len(numList)
for i in range(1, n):
    if numList[i] > numList[i - 1]:
        print(numList[i], end=' ')

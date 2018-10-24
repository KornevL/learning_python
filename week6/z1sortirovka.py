#!/usr/bin/env python3

lenList = int(input())
numList = list(map(int, input().split()))
numList.sort()
print(*numList)

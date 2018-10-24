#!/usr/bin/env python3

N = int(input())
i = 0
squad = 1
squadTWO = 0
while squad < N:
    if squad < N:
        squadTWO = i
    squad = squad * 2
    i = i + 1
print(i)

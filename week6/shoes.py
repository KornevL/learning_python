#!/usr/bin/env python3

size = int(input())
shoesList = list(map(int, input().split()))
shoesList.sort()
lenSL = len(shoesList)
q = 0
if size <= (shoesList[lenSL - 1]):
    i = 0
    while shoesList[i] < size:
        i += 1
    size = shoesList[i]
    sL = [(size)]
    i += 1
    q += 1
    while i != lenSL:
        if (size + 3) <= shoesList[i]:
            q += 1
            size = shoesList[i]
        i += 1
print(q)

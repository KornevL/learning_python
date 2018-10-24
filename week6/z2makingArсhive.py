#!/usr/bin/env python3

memoryANDpersons = list(map(int, input().split()))
memory = memoryANDpersons[0]
numPerson = memoryANDpersons[1]
memtoper = []
i = 0
while i < numPerson:
    memtoper.append(int(input()))
    i += 1
memtoper.sort()
summ = 0
i = 0
while summ <= memory and i < numPerson:
    if summ + memtoper[i] > memory:
        break
    summ += memtoper[i]
    i += 1
print(i)

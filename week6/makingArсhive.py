#!/usr/bin/env python3

a = 'Memory of base data and quantity of clients: '
memoryANDpersons = list(map(int, input(a).split()))
memory = memoryANDpersons[0]
print('Memory =', memory)
numPerson = memoryANDpersons[1]
print('Quantity of clients =', numPerson)
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
print(summ, '- summ of client\'s data')
print(i, '- max possible quantity client of base data')

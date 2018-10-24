#!/usr/bin/env python3

inFile = open('input.txt', 'r', encoding='utf-8')
sumN = 0
N = 0
sumT = 0
T = 0
sumE = 0
E = 0
for line in inFile:
    line = line.split(' ')
    if int(line[2]) == 9:
        sumN += int(line[-1])
        N += 1
    elif int(line[2]) == 10:
        sumT += int(line[-1])
        T += 1
    else:
        sumE += int(line[-1])
        E += 1
inFile.close()
N = sumN / (N or 1)
T = sumT / (T or 1)
E = sumE / (E or 1)
print(N, T, E)

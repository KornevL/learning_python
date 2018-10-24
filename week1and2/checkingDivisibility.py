#!/usr/bin/env python3

a = int(input())
b = int(input())
answer = a % b
one = (answer == 0)
two = (answer > 0)
printNow = 'YES' * one + 'NO' * two
print(printNow)

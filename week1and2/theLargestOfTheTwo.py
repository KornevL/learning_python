#!/usr/bin/env python3

a = int(input())
b = int(input())
answerOne = a // b
one = (a >= b)
two = (a < b)
printNow = str(a) * one + str(b) * two
print(int(printNow))

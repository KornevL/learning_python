#!/usr/bin/env python3


def sumOfTHeSequence():
    n = int(input())
    if n != 0:
        return n + sumOfTHeSequence()
    else:
        return 0


print(sumOfTHeSequence())

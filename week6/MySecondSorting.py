#!/usr/bin/env python3


def Intersection(a, b):
    lenA = len(a)
    lenB = len(b)
    mL = []
    i = 0
    j = 0
    while i != lenA and j != lenB:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            mL.append(a[i])
            i += 1
            j += 1
    return mL


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*Intersection(a, b))

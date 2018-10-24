#!/usr/bin/env python3


def merge(a, b):
    lenA = len(a)
    lenB = len(b)
    mL = []
    i = 0
    j = 0
    while i != lenA and j != lenB:
        if a[i] < b[j]:
            mL.append(a[i])
            i += 1
        elif a[i] > b[j]:
            mL.append(b[j])
            j += 1
        else:
            mL.append(a[i])
            i += 1
            mL.append(b[j])
            j += 1
    if i == lenA:
        mL.extend(b[j:])
    else:
        mL.extend(a[i:])
    return mL


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))

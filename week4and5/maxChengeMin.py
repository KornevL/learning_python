#!/usr/bin/env python3

nL = list(map(int, input().split()))
min = nL[0]
max = nL[0]
mii = 0
mai = 0
i = 1
while i < len(nL):
    if nL[i] < min:
        min = nL[i]
        mii = i
    if nL[i] > max:
        max = nL[i]
        mai = i
    i += 1
nL.pop(mai)
nL.insert(mai, min)
nL.pop(mii)
nL.insert(mii, max)
print(*nL)

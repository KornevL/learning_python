#!/usr/bin/env python3

homes = int(input())
distHomes = list(map(int, input().split()))
for i in range(homes):
    distHomes[i] = [distHomes[i], i + 1, 0]
distHomes.sort()

saves = int(input())
distSaves = list(map(int, input().split()))
for i in range(saves):
    distSaves[i] = [distSaves[i], i + 1]
distSaves.sort()

numStartSearch = 0

for i in range(homes):
    indexBomb = 0
    minDist = 10000000000
    for j in range(numStartSearch, saves):
        dist = abs(distHomes[i][0] - distSaves[j][0])
        if dist < minDist:
            indexBomb = j
            minDist = dist
            distHomes[i][2] = distSaves[j][1]
        else:
            break
    numStartSearch = indexBomb

distHomes.sort(key=lambda idx: idx[1])
for i in range(homes):
    print(distHomes[i][2], end=' ')

#!/usr/bin/env python3
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
candidates = {}
candidatesList = []
golosov = 0
for line in inFile:
    golosov += 1
    cond = line.rstrip()
    candidates[cond] = candidates.get(cond, 0) + 1
for word in candidates:
    candidatesList.append((-candidates[word], word))
candidatesList.sort()
if int(abs(candidatesList[0][0])) > (golosov / 2):
    print(candidatesList[0][1], file=outFile)
else:
    print(candidatesList[0][1], candidatesList[1][1], sep='\n', file=outFile)
inFile.close()
outFile.close()

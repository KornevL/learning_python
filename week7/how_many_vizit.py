#!/usr/bin/env python3

inFile = open('input.txt', 'r', encoding='utf8')
words = {}
ans = []
for line in inFile:
    for word in line.split():
        ans.append(words.get(word, 0))
        words[word] = words.get(word, 0) + 1
print(*ans)
inFile.close()

#!/usr/bin/env python3
inFile = open('input.txt', 'r', encoding='utf8')
words = {}
wordsList = []
for line in inFile:
    for word in line.split():
        words[word] = words.get(word, 0) + 1
for word in words:
    wordsList.append((-words[word], word))
wordsList.sort()
for slovo in wordsList:
    print(slovo[1])
inFile.close()

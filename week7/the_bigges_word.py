#!/usr/bin/env python3
inFile = open('input.txt', 'r', encoding='utf8')
words = {}
for line in inFile:
    for word in line.split():
        words[word] = words.get(word, 0) + 1
max_count = max(words.values())
most_frequent = [k for k, v in words.items() if v == max_count]
print(min(most_frequent))
inFile.close()

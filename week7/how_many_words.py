#!/usr/bin/env python3
import sys
# inFile = open('input_text.txt', 'r', encoding='utf8')
inFile = sys.stdin  # any file in input
words = set()
for line in inFile:
    words.update(set(line.split()))
print(len(words))
inFile.close()

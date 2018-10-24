#!/usr/bin/env python3

synonyms = {}
how_many_pars = int(input())
for _ in range(how_many_pars):
    syn = list(input().split())
    synonyms[syn[0]] = syn[1]
    synonyms[syn[1]] = syn[0]
search_synonym = input()
print(synonyms[search_synonym])

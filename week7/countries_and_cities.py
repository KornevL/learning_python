#!/usr/bin/env python3

how_many_counries = int(input())
slovar = {}
for _ in range(how_many_counries):
    another_country = []
    another_country = input().split()
    country = another_country[0]
    for i in range(1, len(another_country)):
        slovar[another_country[i]] = country

ans = []
how_many_ans = int(input())
for _ in range(how_many_ans):
        ans.append(slovar[input()])

for i in range(how_many_ans):
    print(ans[i])

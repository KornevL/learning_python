#!/usr/bin/env python3


def clrnumber(clearnum):
    clearnum = clearnum.replace('-', '')
    clearnum = clearnum.replace('+7', '8')
    clearnum = clearnum.replace('(', '')
    clearnum = clearnum.replace(')', '')
    if len(clearnum) == 7:
        clearnum = '8495' + clearnum
    return clearnum

input_number = clrnumber(input())
ans = []

for _ in range(3):
    verifiable_number = clrnumber(input())
    if input_number == verifiable_number:
        ans.append('YES')
    else:
        ans.append("NO")

for i in range(3):
    print(ans[i])

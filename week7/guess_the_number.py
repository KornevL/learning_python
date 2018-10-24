#!/usr/bin/env python3

augus_num = set(range(1, int(input())+1))
ask = list(map(int, input().split()))
while str(ask) != '[\'HELP\']':
    beatris_num = set(list(map(int, ask)))
    if input() == 'YES':
        augus_num &= beatris_num
    else:
        augus_num -= beatris_num
    ask = input().split()
print(*sorted(augus_num, key=int))

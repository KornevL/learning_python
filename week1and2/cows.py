#!/usr/bin/env python3

a = int(input())
print(a, end='')
check = a % 10
if check == 0 or 5 <= check <= 9 or 11 <= a <= 14:
    print(' korov')
elif check == 1:
    print(' korova')
else:
    print(' korovy')

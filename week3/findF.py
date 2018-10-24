#!/usr/bin/env python3

s = input()
first = s.find('f')
length = len(s)
s = s[::-1]
last = s.find('f')
last = length - last - 1
check = first != last
ckeck = first != -1
print(str(first) * ckeck, str(last) * check * ckeck)

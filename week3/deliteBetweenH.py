#!/usr/bin/env python3

s = input()
first = s.find('h')
length = len(s)
ass = s[::-1]
last = ass.find('h')
last = length - last - 1
out = s[:first] + s[last+1:]
print(out)

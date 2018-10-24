#!/usr/bin/env python3

i = 0
n_1 = 0
n_2 = 1
Fn = 0
F = int(input())
while Fn < F:
    Fn = n_1 + n_2
    n_2 = n_1
    n_1 = Fn
    i += 1
if Fn == F:
    print(i)
else:
    print(-1)

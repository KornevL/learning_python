#!/usr/bin/env python3

import math
a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
c1 = float(input())
c2 = float(input())
x = (b1 * c2 - b2 * c1) / (a2 * b1 - a1 * b2)
y = (a2 * c1 - a1 * c2) / (a2 * b1 - a1 * b2)
print(x, y)

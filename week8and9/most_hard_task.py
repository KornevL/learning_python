#!/usr/bin/env python3
from itertools import starmap

print(
    *starmap(
        lambda x, y: abs(int(x) - int(y)),
        zip(
            input().split(),
            input().split()
        )
    )
)

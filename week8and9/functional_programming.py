#!/usr/bin/env python3
from functools import reduce
import sys

print(
    len(
        set(
            reduce(
                lambda x, y: x + y,
                list(
                    sys.stdin
                )
            ).split()
        )
    )
)

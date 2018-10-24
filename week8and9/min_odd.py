#!/usr/bin/env python3

print(
    min(
        filter(
            lambda x: x % 2 != 0,
            map(
                int,
                input().split()
            )
        )
    )
)

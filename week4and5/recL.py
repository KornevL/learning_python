#!/usr/bin/env python3


def recL():
    n = int(input())
    if n != 0:
        recL()
        print(n)
    else:
        print(n)
recL()

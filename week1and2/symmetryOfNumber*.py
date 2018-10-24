#!/usr/bin/env python3

a = int(input())
checkingThousand = int(a // 1000)
checkingHundred = int((a // 100) % 10)
checkingTens = int((a // 10) % 10)
ones = a % 10
trigger = (checkingThousand == ones) * (checkingHundred == checkingTens)
print(trigger)

#!/usr/bin/env python3

# p - interest rate
p = int(input())
# x - how many rubles you have
x = int(input())
# y - how many pennies you have
y = int(input())
# k - deposit term in years
k = int(input())
while k > 0:
    moneyIn = x * 100 + y
    moneyOut = moneyIn * (100 + p) / 100
    x = int(moneyOut // 100)
    y = int(moneyOut % 100)
    k -= 1
print(x, y)

#!/usr/bin/env python3

h = int(input())
a = int(input())
b = int(input())
dayNight = a - b
days = (h - a) / dayNight + 1
# print(days)
# to express in round numbers in big side
trigger = days % 1
# print(trigger)
# if days is integer trigger = 0, or else 1 > trigger > 0
trigger = ((trigger + 2) // (trigger + 1))
# print(trigger)
# if days is integer trigger = 2, or else trigger = 1
trigger = trigger % 2
# print(trigger)
# if days is integer trigger = 0, or else trigger = 1
print(int(days // 1 + trigger))

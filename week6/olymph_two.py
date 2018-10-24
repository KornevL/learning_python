#!/usr/bin/env python3

quantity = int(input())
students = []

for i in range(quantity):
    person = input().split(' ')
    students.append(person)

students.sort(key=lambda idx: int(idx[1]))

for i in range((quantity - 1), - 1, -1):
    print(students[i][0])

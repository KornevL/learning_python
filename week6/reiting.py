#!/usr/bin/env python3
def reiting(n, k, konkurs):
    if n <= k:
        return 0
    elif konkurs[k] == konkurs[0]:
        return 1
    for i in range(k, 0, -1):
        if konkurs[i] < konkurs[i - 1]:
            return konkurs[i - 1]

"""
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9FHfN/prokhodnoi-ball
http://www.cyberforum.ru/python/thread2030212.html
"""
inFile = open('input.txt', 'r', encoding='utf8')
k_quantity = int(inFile.readline())
studentList = []

for line in inFile:
    line = line.split()
    student = ()
    if int(line[-1]) >= 40 and int(line[-2]) >= 40 and int(line[-3]) >= 40:
        student = (int(line[-1]) + int(line[-2]) + int(line[-3]))
        studentList.append(student)

inFile.close()
studentList.sort(key=lambda stud: int(-stud))
n_summ_of_pass_stud = len(studentList)

print(reiting(n_summ_of_pass_stud, k_quantity, studentList))

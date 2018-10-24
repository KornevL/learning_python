#!/usr/bin/env python3
class Student:
    secondName = ''
    name = ''
    school = 0
    score = 0

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

studentList = []
for line in inFile:
    line = line.split(' ')
    student = Student()
    student.secondName = line[0]
    student.name = line[1]
    student.school = int(line[2])
    student.score = int(line[3])
    studentList.append(student)

studentList.sort(key=lambda student: student.secondName)
for student in studentList:
    print(student.secondName, student.name, student.score, file=outFile)

outFile.close()
inFile.close()

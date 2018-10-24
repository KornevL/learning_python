#!/usr/bin/env python3
# the number of seconds is entered

sec = int(input())
hours = (sec // 3600) % 24
minutesTens = ((sec % 3600) // 60) // 10
minutesUnits = ((sec % 3600) // 60) % 10
minutes = str(minutesTens) + str(minutesUnits)
secondTens = (sec % 60) // 10
secondUnits = (sec % 60) % 10
seconds = str(secondTens) + str(secondUnits)

print(hours, minutes, seconds, sep=(':'))

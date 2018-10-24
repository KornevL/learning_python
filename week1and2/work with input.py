#!/usr/bin/env python3

print('Who ask me?')
name = input()
print('Hello, ', name, '!', sep='')
print('How many fingers on your right hand?')
rightHand = int(input())
print('Nice!')
print('How many fingers on your left hand?')
leftHand = int(input())
summ = rightHand + leftHand
print('So.. You have', summ, 'fingers, my friend.')
word = 'Bye '
phrase = word * 3 + '!'
print(phrase)

#!/usr/bin/env python3
def CountSort(inp_list):

    box_numb = [0] * 101
    for number in inp_list:
        box_numb[number] += 1
    for now_number in range(101):
        print((str(now_number) + ' ') * box_numb[now_number], end='')

numbers = list(map(int, input().split()))
CountSort(numbers)

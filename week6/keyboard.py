#!/usr/bin/env python3
def CountSort(nums, can, clik):

    box_nums = [0] * (nums + 1)
    for number in clik:
        box_nums[number] += 1
    for now_number in range(1, nums + 1):
        if box_nums[now_number] > can[now_number - 1]:
            print('YES')
        else:
            print('NO')
how_much_num = int(input())
how_much_can = list(map(int, input().split()))
sum_klick = int(input())
klicks = list(map(int, input().split()))
CountSort(how_much_num, how_much_can, klicks)

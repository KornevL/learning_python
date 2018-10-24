#!/usr/bin/env python3

from itertools import combinations, permutations, combinations_with_replacement
from functools import partial

# тут функция, нумерующая входящие в нее элементы
f = open('data.txt', 'r', encoding='utf8')
tyu = enumerate(f)
print(tyu, type(tyu))
for i, line in enumerate(f):
    print(i, line.rstrip())

# itertools.combinations(iterable, size) -
# генерирует все подмножества множества iterable размером
# size в виде кортежей. Это может быть использовано вместо
# вложенных циклов при организации перебора. Например,
# мы можем неэффективно решить задачу о поиске трех чисел в
# последовательности, дающих наибольшее произведение:

nums = list(map(int, input().split()))
combs = combinations(range(len(nums)), 3)
print(max(map(lambda x: nums[x[0]] * nums[x[1]] * nums[x[2]], combs)))

q_f = 'что в перестановку?\n'
q_s = 'по сколько делить?\n'
fuck = permutations(range(int(input(q_f)) + 1), int(input(q_s)))
print(*fuck, type(fuck))

q_f = 'что в перестановку с повторениями?\n'

s = combinations_with_replacement(range(int(input(q_f)) + 1), int(input(q_s)))
print(*s, type(s))

# задает всем функциям шаблон)
binStrToInt = partial(int, base=10)
print(binStrToInt('10010431141441'))

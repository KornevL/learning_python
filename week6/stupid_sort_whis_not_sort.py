#!/usr/bin/env python3
def CountSort(inp_list):
    right_list = [inp_list[0]]
    i = 1
    while i != len(inp_list):
        for j in range(len(right_list)):
            if right_list[j] >= inp_list[i]:
                right_list.insert(j, inp_list[i])
                break
        else:
            right_list.append(inp_list[i])
        i += 1
    return(right_list)

numbers = list(map(int, input().split()))
print(*CountSort(numbers))

def solution(A):
    num_of_castles = 0
    step_left = -1
    A.append(A[-1])
    for i in range(len(A) - 1):
        step = int(A[i + 1]) - int(A[i])
        if step != 0:
            if step > 0:
                step_right = 1
            else:
                step_right = 0
            if (step_right != step_left) or (step_left == -1):
                num_of_castles += 1
                step_left = step_right
    return num_of_castles + 1
print(solution([1, 2, 1, 2, 4]))

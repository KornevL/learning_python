#!/usr/bin/env python3

# INSTRUCTION
# There is a white checker on the board.
# It is required to determine whether it can get into this cell,
# make movements in accordance with the rules (without turning into a lady).
# White checkers can walk on black cells diagonally up-left or up-right.
# Maybe a few steps!
#
# INPUT FORMAT
# Enter the start cage, and then the cage into which the checker should enter.
# Each cell is described by the number of the vertical,
# and then by the number of the horizontal.
#
# OUTPUT FORMAT
# Print the word YES (in capital letters) if the checker can move from the
# starting cell to the specified cell, and NO otherwise.
#
# NOTES
# The board has a size of 8x8, vertical and horizontal numbers are numbered
# from 1 to 8, starting from the lower left corner.
# The start and end cells do not match.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((y2 % 2 == 0 and x2 % 2 == 0) or (y2 % 2 != 0 and x2 % 2 != 0)):
    if (x2 - x1 <= y2 - y1) and (x2 - x1 >= y1 - y2) and y2 > y1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

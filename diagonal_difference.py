## Given a square matrix, calculate the absolute difference between the sums of its diagonals.

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr) # length & height of matrix 
    diff = 0 # running difference
    for i in range (0,n):
        diff = diff + arr[i][i]- arr[i][n-1-i]
    return abs(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

## SCORE RECEIVED: 100.00 / ACCEPTED

## Given a square matrix, calculate the absolute difference between the sums of its diagonals.

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr) # length & height of matrix 
    LRD = RLD = 0 # variables to hold value of left-right and right-left diagonals
    for i in range (0,n):
        LRD = LRD + arr[i][i]
        RLD = RLD + arr[i][n-1-i]
    return abs(LRD-RLD)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

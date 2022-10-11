## Given an array arr with an unknown number of elements and all values being non-negative integers between 0 and 99,
#  return a counting array int of length 100 whose element values correspond to the number of times that index appeared
#  in the original array.

import math
import os
import random
import re
import sys

def countingSort(arr):
    int = [0]*100 
    for i in arr:
        int[i] +=1
    return int

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
## SCORE RECEIVED: 100.00 / ACCEPTED

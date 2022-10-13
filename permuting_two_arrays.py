## Given two n-element arrays of integers (A and B) and an integer k, return YES 
# if they can be permuted in such a way that every element in A can be matched with 
# an element in B for a sum that is greater than or equal to K. Otherwise, return NO

import math
import os
import random
import re
import sys


def twoArrays(k, A, B):
    # Rather than iterating through one array and searching for a match in the other, I sorted
    # one in ascending order and the other in descending order. Since they are of equal length,
    # if ever two corresponding elements do NOT sum to k or more, the function returns 'NO'
    A.sort()
    B.sort()
    B.reverse()
    for i in range (0,len(A)-1):
        if A[i] + B[i] < k: return 'NO'
    return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
# SCORE: 100.0 / ACCEPTED

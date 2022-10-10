# HACKERRANK PROBLEM: Plus Minus -- Given an array of integers, calculate the ratios of its elements that are positive,
# negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

import math
import os
import random
import re
import sys

def plusMinus(arr):
    ## Given INTEGER_ARRAY arr with up to 100 elements
    ## with values between -100 and 100, print ratio of
    ## positive integers, negative integers, and zero.
    
    # Initialize counters
    pos = neg = zero = total = 0
    
    for num in arr:
        if num > 0: pos = pos +1
        elif num < 0: neg = neg + 1
        else: zero = zero +1
        total = total + 1
    
    # Print results as proportion with 6 digits after decimal point
    for x in (pos,neg,zero):
        print(f"{(x/total):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

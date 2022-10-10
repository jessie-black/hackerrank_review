# Mini-Max Sum problem prompt: Given five positive integers, find the minimum and maximum values that can be calculated 
# by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of 
# two space-separated long integers.

# Constraints: element values are between 1 and 10^9, inclusive

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # arr is an array of 5 positive integers between 1 and 10^9
    sorted_array = sorted(arr) # as we know the size of the array is only 5, sorting it will not be a prohibitively slow procedure.
    # print smallest and largest sums of 4 out of 5 elements of array.
    print(sum(sorted_array[0:4]), sum(sorted_array[1:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

## SCORE RECEIVED: 100.00 / ACCEPTED

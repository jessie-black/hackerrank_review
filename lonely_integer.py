## Given an non-empty array with an odd number of integers where all elements but one occur twice, find the single unique element. 
## For examlpe: given a = [1,2,3,4,3,2,1], return 4.

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    unique = [] # new list to hold all numbers encounterd just once
    for n in a:
        if n in unique: unique.remove(n) # if it's already in the list, remove it (we have found a 2nd occurence)
        else: unique.append(n) # otherwise add it (we have found a 1st occurrence)
    return unique[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

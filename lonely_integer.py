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
        unique.remove(n) if n in unique else unique.append(n)
        # if it's already in the list, remove it (we have found a 2nd occurence), otherwise add it (we have found a 1st occurrence)
    return unique[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
## SCORE RECEIVED: 100.00 / ACCEPTED

## My solution works, but requires iterating through the entire array O(n) in all cases. An alternative is to 
# check how many occurrences each element has. It will be substantially faster if element occurs sooner in array. 
#
# def lonelyinteger(a): 
#    for x in a: if a.count(x) == 1 : return x

## More elegant solution posted by johannzen based on logic that if you double the sum of the SET 
# (one of each number, including the unique number) and then subtract the sum of the ARRAY (with 
# duplicates), you are left with the value of the unique element.
#
# def lonelyinteger(a):
#    sum_of_set = sum(set(a))
#    sum_of_list = sum(a)
#   return sum_of_set*2-sum_of_list

## Given a large pile of socks that must be paired by color (represented as integer values in an array), determine how many matching pairs are present.

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pairs = 0
    socks_found = {}                    # initial approach: create a dictionary
    for sock in ar:
        if sock in socks_found:
            socks_found[sock] +=1       # increment value of given key (color integer) every time it is encountered
            if socks_found[sock] == 2:
                pairs += 1              # increment pairs every time we have 2 matching socks
                socks_found[sock]=0     # and then set the value of that key to 0
        else:
             socks_found[sock] = 1      # initialize key with value of 1 if not already present
    return pairs   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

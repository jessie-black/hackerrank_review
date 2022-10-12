# Given a 32-bit unsigned integer in decimal, convert to binary, flip all bits, and returned as unsigned integer in decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    return 4294967295-n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
## SCORE = 100.0, Accepted

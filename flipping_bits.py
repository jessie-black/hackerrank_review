# Given a 32-bit unsigned integer in decimal, convert to binary, flip all bits, and returned as unsigned integer in decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    binary = format(n, 'b') #convert decimal to binary
    for i in range (0,32-len(str(binary))): # prepend leading 0s to ensure 32-bit input
        binary = "0" + binary
    rev_binary = ""
    for i in str(binary):   # flip all bits
        if i=='0': rev_binary+='1'
        else: rev_binary +='0'
    return int(rev_binary,2) # return reversed binary converted to decimal
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
## SCORE = 100.0, Accepted

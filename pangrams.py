## given a string, return 'pangram' if all letters of the alphabet are present (ignoring case), otherwise 'not pangram'

import math
import os
import random
import re
import sys

def pangrams(s):
    string = s.lower()
    for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        if not letter in string: return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
# Score: 100.0 / Accepted

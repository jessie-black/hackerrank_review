## given a string, return 'pangram' if all letters of the alphabet are present (ignoring case), otherwise 'not pangram'

import math
import os
import random
import re
import sys

def pangrams(s):
    letters = set(s.lower().replace(' ',''))
    return 'not pangram' if len(letters)<26 else 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
# Score: 100.0 / Accepted

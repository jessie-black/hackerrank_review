## given a string of only letters and spaces, return 'pangram' if all letters of the alphabet are present (ignoring case), otherwise 'not pangram'

import math
import os
import random
import re
import sys

def pangrams(s):
    # remove any spaces and make a lowercase set of all letters appearing in s. 
    # It cannot be a pangram if there are fewer than 26 letters, so return response accordingly.
    return 'not pangram' if len(set(s.lower().replace(' ','')))<26 else 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
# Score: 100.0 / Accepted

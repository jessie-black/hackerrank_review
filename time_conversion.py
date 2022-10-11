## Given a 12-hour time in AM/PM format, convert it to military time and return as a string.
## Input is a single string  that represents a time in -hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

import math
import os
import random
import re
import sys

def timeConversion(s):
    # s is a STRING which always has format hh:mm:ss_M
    hh = s[0:2]
    # If it is 12:__:__, convert hours to 00 if AM, otherwise leave as is for PM
    if (hh == '12'):
        if (s[-2] == 'A'): hh = '00'
    # For all PM times aside from 12:__:__, add 12 hours to the hour marker
    elif (s[-2] == 'P'): hh = int(hh) + 12
    # All other AM times are left as-is.
    # Combine NEW hh, existing :mm:ss, and cut off AM/PM. Return as STRING
    return (str(hh) + s[2:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

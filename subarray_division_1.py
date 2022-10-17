## Given the prompt: "Two children, Lily and Ron, want to share a chocolate bar. 
#  Each of the squares has an integer on it. Lily decides to share a contiguous 
#  segment of the bar selected such that: The length of the segment matches Ron's 
#  birth month, and, The sum of the integers on the squares is equal to his birth day.
#  Determine how many ways she can divide the chocolate."
#
#  Fixed solution to accomodate *CONTIGUOUS* referring to elements and not segments within each element.
import math
import os
import random
import re
import sys
import itertools

def birthday(s, d, m):
    #!/bin/python3

import math
import os
import random
import re
import sys
import itertools

def birthday(s, d, m):
    # goal: return int representing how many sets of 
    # m contiguous elements of s add up to d
    n = len(s)
    if n<m: return 0 # there is no possible solution if there are fewer than m segments.
    tally = 0
    window_sum = sum(s[:m]) # get the sum of the first m elements
    if window_sum == d: tally += 1
    for i in range(n-m): # for all remaining potential windows
        window_sum = window_sum - s[i] + s[i+m] #remove earlier segemnt, add later segment
        if window_sum == d: tally += 1
    return tally

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
    
## Score: 100.0 / Accepted

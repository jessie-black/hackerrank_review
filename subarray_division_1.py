## Given the prompt: "Two children, Lily and Ron, want to share a chocolate bar. 
#  Each of the squares has an integer on it. Lily decides to share a contiguous 
#  segment of the bar selected such that: The length of the segment matches Ron's 
#  birth month, and, The sum of the integers on the squares is equal to his birth day.
#  Determine how many ways she can divide the chocolate."
#
#  I interpreted the purpose of this as: given an array s of integers, 
#  as well as integers d and m, return an int representing how many combinations
#  of m elements from s add up to a total sum equal to d. 
import math
import os
import random
import re
import sys
import itertools

def birthday(s, d, m):
    tally = 0
    all_combinations = set(itertools.combinations(s,m))
    # Get a set of combinations so that there are no duplicates 
    for i in all_combinations:
        if sum(i) == d: tally +=1
        # Add one to the tally for every group that has the correct sum
    return tally # Return the final count representing all possible correct answers.
  
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
    
## THIS solution worked for the 3 sample cases but failed most of the test cases. 
#  I was struggling to understand what I had done wrong. I reworked it and came 
#  to the same general approach, and then re-reading the prompt multiple times I 
#  realize I had misinterpreted 'continguous' to mean the segments already grouped
#  into elements of s when in reality the problem was asking for continguous ELEMENTS
#  of s. (This would have been a situation in which it would have been great to have
#  a human to confirm that my understanding was accurate...). Reworking in followup.

## Given input of two arrays of strings, 'strings' and 'queries', output an array of integers
#   with the number of how many times each word from 'queries' appears in 'strings'. Some words 
#   may not appear at all, and should have a corresponding 0 in final array.

import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    n= len(queries)
    tally = [0] * n # create an array of integers as long as the queries array, all initialized to 0
    for i in range(0,n):
        tally[i] = strings.count(queries[i])  # update with correct count for all values in 'strings'
    return tally   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
## SCORE RECEIVED: 100.00 / ACCEPTED

## Observations: My first instinct was to create a dictionary with strings from 'queries' 
#  as keys and initialize all values to 0, incrementing by 1 for every word in 'strings'
#  ... However, for some reason this approach passed the initial 3 test cases but failed the 13 
#  later test cases upon submission. Created this alternative appraoch.


## More elegant solution by user VictorSGhosh: 
#  def matchingStrings(strings, queries):
#      return [strings.count (1) for q in queries]
# This is the kind of concise code that I would like to write more of in python. I'm always
# astonished by how efficient python can be in terms of lines of code! It is still not intuitive
# for me to write this concisely BUT I do find I am getting better at refactoring after 
# writing out initial thoughts/approach.

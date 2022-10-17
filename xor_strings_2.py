## This was a very simple assignment to debug the following to print a XOR string of the input:
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] = t[i]: # This is an assignment, it should be a comparison
            res = '0';  # This should ADD a zero to the existing string res, not replace it.
        else:
            res = '1';  # Similarly, this should add a 1 rather than replacing.

    return res

s = input()
t = input()
print(strings_xor(s, t))
## ANALYSIS: Because the buggy version above always assigns s[i] to be equivalent to t[i], 
#  the statement res = '0' will always be performed (repeatedly, for all elements in s) and 
#  the final output will always be 0 regardless of input.

## My solution: 
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))
# SCORE: 100.0 / Submission accepted.

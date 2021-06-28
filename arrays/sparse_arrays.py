#!/bin/python3

'''
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

Example
strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']


There are  instances of ',  of '' and  of ''. For each query, add an element to the return array, .
results = [2, 1, 0]

Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings

Returns
int[q]: an array of results for each query

Input Format

The first line contains and integer , the size of .
Each of the next  lines contains a string .
The next line contains , the size of .
Each of the next  lines contains a string .

Constraints
1<= n <= 1000
1<= q <= 1000
1<= |strings[i]|, |queries[i]| <= 20

'''

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'matchingStrings' function below.
#

#

def matchingStrings(strings: List[str], queries: List[str]) -> List[int]:
    '''
    The function is expected to return an INTEGER_ARRAY.
    The function accepts following parameters:
    1. STRING_ARRAY strings
    2. STRING_ARRAY queries
    '''
    string_dict = dict()
    for s in strings:
        string_dict[s] = string_dict.get(s,0) + 1
    ret = [string_dict.get(q,0) for q in queries]
    return ret

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

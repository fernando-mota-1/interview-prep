import math
# Add any extra import statements you may need here
from itertools import combinations


# Add any helper functions you may need here


def matching_pairs(s, t):
  # Write your code here
  combos = combinations(range(len(s)), 2)
  c = list(combos)
  counter = [0]*len(c)
  for ind,(i,j) in enumerate(c):
    new_s = s[:i] + s[j] + s[i+1:j] + s[i]+ s[j+1:]
    for k, val in enumerate(t):
      if new_s[k] == val:
        counter[ind] += 1
  return max(counter)
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
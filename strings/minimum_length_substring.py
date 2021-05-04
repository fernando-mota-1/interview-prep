import math
# Add any extra import statements you may need here
from collections import Counter

# Add any helper functions you may need here


def min_length_substring(s, t):
  # Write your code here
  res = -1
  len_t = len(t)
  t_counter = Counter(list(t))
  s_counter = Counter(list(s[:len_t]))
  needed_items = t_counter.keys()
  still_needed = set(needed_items)
  for item in needed_items:
    if s_counter[item] == t_counter[item]:
      still_needed.remove(item)
  if not still_needed:
    res = len_t
  else:
    for i, val in enumerate(s[len_t:]):
      s_counter[val] += 1
      needed_items = set(still_needed)
      for item in needed_items:
        if s_counter[item] == t_counter[item]:
          still_needed.remove(item)
      if not still_needed:
        res = len_t + i + 1
        break
  
  return res
  
	











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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

	# Add your own test cases here
  
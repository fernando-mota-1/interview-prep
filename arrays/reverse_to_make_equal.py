import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  # Write your code here
  res = True
  set_a, set_b = set(array_a), set(array_b)
  if set_a.symmetric_difference(set_b):
    res = False
  else:
    res = sorted(array_a) == sorted(array_b)
  return res










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  n_3 = 8
  a_3 = [1,2,8,5,9,2,9,9]
  b_3 = [2,1,8,5,9,2,9,2]
  expected_3 = False
  output_3 = are_they_equal(a_3, b_3)
  check(expected_3, output_3)
  
  n_4 = 8
  a_4 = [1,2,8,5,9,2,9,9]
  b_4 = [2,1,8,9,9,2,9,5]
  expected_4 = True
  output_4 = are_they_equal(a_4, b_4)
  check(expected_4, output_4)
  
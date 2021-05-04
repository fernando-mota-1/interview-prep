import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
  # Write your code here
  s_arr = sorted(arr)
  for i in range(len(s_arr)-1):
    a = sum(s_arr[:i+1])
    b = sum(s_arr[i+1:])
    if a == b:
      return True if s_arr[i] != s_arr[i+1] else False
  
  return False
  










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
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
  arr_3 = [12, 7, 6, 7, 6]
  expected_3 = False
  output_3 = balancedSplitExists(arr_3)
  check(expected_3, output_3)
  
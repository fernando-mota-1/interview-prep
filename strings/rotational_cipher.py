import math
# Add any extra import statements you may need here
import string

# Add any helper functions you may need here

def gen_worker(input, rotation_factor):
  for i in input:
    if i in string.digits:
      rot = (rotation_factor + string.digits.index(i)) % len(string.digits)
      out = string.digits[rot]
    elif i in string.ascii_lowercase:
      rot = (rotation_factor + string.ascii_lowercase.index(i)) % len(string.ascii_lowercase)
      out = string.ascii_lowercase[rot]
    elif i in string.ascii_uppercase:
      rot = (rotation_factor + string.ascii_uppercase.index(i)) % len(string.ascii_uppercase)
      out = string.ascii_uppercase[rot]
    else:
      out = i
      
    yield out
  


def rotationalCipher(input, rotation_factor):
  # Write your code here
  gen = gen_worker(input, rotation_factor)
  return ''.join(list(gen))
    
  



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
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)
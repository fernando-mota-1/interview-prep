'''
Run Length Encoding

A way to encode a file is to represent characters with a counter. This is more efficient when
there are lots of consecutive duplicate characters

Signature
string string_encode(string input)

Input
1 <= input.length() <= 1,000,000

Output
return a string that represents the encoded version

Example 1
input = aaaabbcdd
output = 4a2b1c2d

Example 2
input = bbcccdeeffff
output = 2b3c1d2e4f
'''

def string_encode(input):
  # string builder
  res = ''

  # None or empty check
  if input:
    prevCh = None
    counter = 0

    # iteration for string builder
    for ch in input:
      if ch == prevCh:
        counter += 1
      else:
        if prevCh:
          res += f'{counter}{prevCh}'
        counter = 1
        prevCh = ch
    res += f'{counter}{prevCh}'
  
  # return the string builder
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
  input_1 = "aaaabbcdd"
  expected_1 = "4a2b1c2d"
  output_1 = string_encode(input_1)
  check(expected_1, output_1)

  input_2 = "bbcccdeeffff"
  expected_2 = "2b3c1d2e4f"
  output_2 = string_encode(input_2)
  check(expected_2, output_2)
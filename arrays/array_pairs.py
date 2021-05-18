'''
Consider an array of n integers, A=[a1,a2,...an]. Find and print the total number of (i,j) pairs such that ai x aj <= max(ai,ai+1,...aj) where i<j.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line consists of  space-separated integers describing the respective values of .

Constraints
1 <= n <= 5*10^5
1 <= ai <= 10^9

Scoring

 1 <= n <= 1000 for 25% of the test cases.
 1 <= n <= 10^5 for 50% of the test cases.
 1 <= n <= 5*10^5 for 100% of the test cases.
Output Format

Print a long integer denoting the total number (i,j) pairs satisfying ai x aj <= max(ai,ai+1,...aj) where i<j.

Sample Input

5  
1 1 2 4 2
Sample Output

8
'''

def solve(arr):
    # Write your code here
    sz = len(arr)
    mx = arr[0]
    counter = 0
    for i in range(sz-1):
        mx = arr[i]
        if arr[i] == 1:
            counter += sz-1 - i
            continue
        for j in range(i+1, sz):
            if arr[j] > mx:
                mx = arr[j]
            if arr[i]*arr[j] <= mx:
                counter += 1
    return counter


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
  input_1 = [1,1,2,4,2]
  expected_1 = 8
  output_1 = solve(input_1)
  check(expected_1, output_1)

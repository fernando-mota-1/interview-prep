'''
    Practice test for finding three numbers that sum to zero
'''
from typing import Iterable


def three_sum_zero(arr: Iterable):
    '''
    returns 3 numbers that sum to zero else None
    '''
    if arr and len(arr) > 2:
        arr.sort()
        for i in range(0, len(arr)-2):
            left = i + 1
            right = len(arr) - 1
            while left < right:
                tot = arr[i] + arr[left] + arr[right]
                if tot == 0:
                    return [arr[i], arr[left], arr[right]]
                elif tot > 0:
                    right -= 1
                else:
                    left += 1
    return None


if __name__ == "__main__":
    test_cases = [
        [2, 4, 5, -6, -3, 4, 1, 8],
        [1, -1],
        [-1, 2, 0, -3, -2],
        None,
        [3, 4, 5, 6, 7, 8, -1]
    ]
    for test in test_cases:
        print(f"Test: {test} -> {three_sum_zero(test)}")

"""
KATA DESCRIPTION
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""

import test
from sys import exit

def max_sequence(a):
    iter_a = iter(a)
    try:
        temp = next(iter_a)
    except StopIteration:
        temp = 0
    m = temp
    for item in iter_a:
        temp = max(temp + item, item)
        m = max(temp, m)
    return max(m, 0)

def main():
    test.assert_equals(max_sequence([]), 0, "Should work on an empty array")
    test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6,"Should obtain correct maximum subarray sum in the array from the kata description example")
    test.assert_equals(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0, "Should obtain correct maximum subarray sum in an example with negative numbers")
    test.assert_equals(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155, "Should obtain correct maximum subarray sum in a complex example") 

if __name__ == "__main__":
    main()

exit()

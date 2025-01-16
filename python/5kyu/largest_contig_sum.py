"""
Kata Description:
    Given an array of numbers, calculate the largest sum of all possible blocks of consecutive elements within the array. The numbers will be a mix of positive and negative values. If all numbers of the sequence are nonnegative, the answer will be the sum of the entire array. If all numbers in the array are negative, your algorithm should return zero. Similarly, an empty array should result in a zero return from your algorithm.

largestSum([-1,-2,-3]) == 0
largestSum([]) == 0
largestSum([1,2,3]) == 6

Easy, right? This becomes a lot more interesting with a mix of positive and negative numbers:

largestSum([31,-41,59,26,-53,58,97,-93,-23,84]) == 187

The largest sum comes from elements in positions 3 through 7: 59+26+(-53)+58+97 == 187

Once your algorithm works with these, the test-cases will try your submission with increasingly larger random problem sizes.
"""

import test
from sys import exit

def largest_sum(l):
    # Kadane's algorithm
    # See https://www.geeksforgeeks.org/largest-sum-contiguous-subarray-in-c/#
    if l == []:
        return 0

    max_out = 0
    max_temp = 0
    for i in range(0, len(l)):
        max_temp = max(l[i], max_temp+l[i])
        max_out = max(max_out, max_temp)

    return max_out

def main():
    test.assert_equals(largest_sum([-1,-2,-3]), 0)
    test.assert_equals(largest_sum([]), 0)
    test.assert_equals(largest_sum([1,2,3,4]), 10)
    test.assert_equals(largest_sum([31,-41,59,26,-53,58,97,-93,-23,84]), 187)

if __name__ == "__main__":
    main()

exit()

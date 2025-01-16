"""
Kata Description:

"""
import test
from sys import exit

def largest_radial_sum(arr, d):
    """
    Computes max sum of d entries with values in arr spaced evenly around a
    circular table of len(arr).
    Fill a dictionary with the needed sums, then find the max of the sum.
    Use a dictionary because there are multiple 'local' sums to keep track of
    whilst looking for the global sum.
    O(n), only move through the array 1x + one call to max of the dict values."""
    max_loc = {}
    mesh  = int(len(arr) / d)
    for i in range(0,len(arr)):
        try:
            max_loc[i % mesh] += arr[i]
        except KeyError:
            max_loc[i % mesh] = arr[i]


    return max(max_loc.values())

def main():
    sample_test_cases = [
    #   arr               d  expected
    ([1, 2, 3, 4],        2,    6),
    ([1, 5, 6, 3, 4, 2],  3,   11),
    ([1, 1, 0],           1,    1),]
    for arr, d, expected in sample_test_cases:
        test.assert_equals(largest_radial_sum(arr, d), expected)

if __name__ == "__main__":
    main()

exit()

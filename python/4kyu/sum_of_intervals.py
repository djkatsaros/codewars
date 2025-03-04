"""
Kata Description
Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
Intervals

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
Overlapping Intervals

List containing overlapping intervals:

[
   [1, 4],
   [7, 10],
   [3, 5]
]

The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
Examples:

sumIntervals( [
   [1, 2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030

Tests with large intervals

Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range [-1000000000, 1000000000].

"""

import test

def sum_of_intervals(intervals):

    intvls = list(map(list, intervals))
    stack = []

    if len(intvls) > 0:
        intvls.sort()
        stack = []

        # insert first interval in the stack
        stack.append(intvls[0])

        # check for overlapping interval
        for i in intvls[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
    else:
        stack.append(intvls)

    s = 0
    for i in stack:
        s += i[1] - i[0]

    return s

def main():
    test.assert_equals(sum_of_intervals([(1, 5)]), 4)
    test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
    test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
    test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
    test.assert_equals(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
    test.assert_equals(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)

if __name__ == "__main__":
    main()

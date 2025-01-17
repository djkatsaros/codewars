""" 
Kata Description
You are given a number sequence (an array) that contains some positive integer and zero.

[3,2,1,0,5,6,4,0,1,5,3,0,4,2,8,0]

It can be split to some zero-terminated sub sequence, such as [3,2,1,0], [5,6,4,0] ..

Your task is: First, sort each sub sequence according to the ascending order (don't sort the zero, it always at the end); Second, sort all sub sequence according to their sum value (ascending order too).

    Arguments:
        sequence: The number sequence.

    Results & Note:
        The result is the sorted number sequence.
        If some sub sequences have the same sum value, sort them according to their original order.

"""

import test
from sys import exit

def sort_sequence(seq):
    """ step 1: Create list of tuples (sum, sequence) based on lcoation of 0's
        step 2: Sort the tuples by the sum and concatenate into a list of the actual
        values
        O(n) algorithm:
                iterate through the seq 1x sorting 3 element chunks along the way = 3*n,
                plus sorting by the first tuple entry,
                plus iterate through tuples 1x, appending 4 values at each step = 4*n"""

    outs = []
    last = 0
    idx = 0

    while idx < len(seq):
        if seq[idx] == 0:
            outs.append((sum(seq[last:idx]), sorted(seq[last:idx]) + [0])) # easier to append 0 then jump that idx
            idx += 1 # skip this index
            last = idx
        idx += 1

    ans = []
    for (s, ls) in sorted(outs, key = lambda tup: tup[0]):
        for  val in ls:
            ans.append(val)
    return ans

def main():
    a = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
    r = [1, 2, 3, 0, 1, 3, 5, 0, 2, 4, 8, 0, 4, 5, 6, 0]
    test.assert_equals(sort_sequence(a), r)

    a = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 2, 2, 2, 0]
    r = [1, 2, 3, 0, 2, 2, 2, 0, 1, 3, 5, 0, 4, 5, 6, 0]
    test.assert_equals(sort_sequence(a), r)

    a = [2, 2, 2, 0, 5, 6, 4, 0, 1, 5, 3, 0, 3, 2, 1, 0]
    r = [2, 2, 2, 0, 1, 2, 3, 0, 1, 3, 5, 0, 4, 5, 6, 0]
    test.assert_equals(sort_sequence(a), r)

if __name__ == "__main__":
    main()

exit()

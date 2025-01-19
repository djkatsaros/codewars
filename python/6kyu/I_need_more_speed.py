"""
Kata Description

Write a function that will take in any array and reverse it.

Sounds simple doesn't it?

NOTES:

    Array should be reversed in place! (no need to return it)
    Usual builtins have been deactivated. Don't count on them.
    You'll have to do it fast enough, so think about performances


"""

import test
from sys import exit

import math

def reverse(seq):
    """As I walk the streets of Cairo / I empathize as I go
    / And I feel ashamed / Of the land from where I came"""
    end = len(seq)-1
    for i in range(math.ceil((end+1) / 2)):
        temp = seq[i]
        seq[i] = seq[end - i]
        seq[end-i] = temp


    return seq

def main():
    seq = [1,2,3,4,5]
    reverse(seq)
    test.assert_equals(seq,[5,4,3,2,1])

    seq = ['?','you','are','how','world','hello']
    reverse(seq)
    test.assert_equals(seq,['hello','world','how','are','you','?'])

    seq = [{'b':2},{'a':1}]
    reverse(seq)
    test.assert_equals(seq,[{'a':1},{'b':2}])

if __name__ == "__main__":
    main()

exit()

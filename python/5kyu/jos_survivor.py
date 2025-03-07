"""
Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:

n=7, k=3 => means 7 people in a circle
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!

The above link about the "base" kata description will give you a more thorough insight about the origin of this kind of permutation, but basically that's all that there is to know to solve this kata.

Notes and tips: using the solution to the other kata to check your function may be helpful, but as much larger numbers will be used, using an array/list to compute the number of the survivor may be too slow; you may assume that both n and k will always be >=1.
"""

import test
from sys import exit

# use old function

def josephus(jos ,k):
    """Mostly just appropriate use of % and visualization"""
    out = []
    if jos:
        curr = (k - 1) % len(jos)
        while jos:
            out += [jos.pop(curr)]
            if jos:
                curr = (curr + k - 1) % len(jos)
    return out

def josephus_survivor(n,k):
    return josephus(list(range(1,n+1)),k)[-1]

def main():
    test.assert_equals(josephus_survivor(7,3),4)
    test.assert_equals(josephus_survivor(11,19),10)
    test.assert_equals(josephus_survivor(1,300),1)
    test.assert_equals(josephus_survivor(14,2),13)
    test.assert_equals(josephus_survivor(100,1),100)

if __name__ == "__main__":
    main()

exit()

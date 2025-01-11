"""
KATA DESCRIPTION
Sum of Pairs

Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * the correct answer is the pair whose second value has the smallest index
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined/Nothing (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * the correct answer is the pair whose second value has the smallest index
== [3, 7]

Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""

from sys import exit
import test

def sum_pairs(l, s):
    """sets make this fast enough, as searching sets is O(1)
     Key to the algorithm is looking for the needed difference in the entries already passed in the loop
     These entries are stored in a set, added one by one in the loop each
     time we don't find the needed difference.
     This ensures we find the first instance of the needed sum (later instances being pairings with
     the number furthest into the list)
     """
    _set = set()
    _set.add(l[0])
    for i in range(1, len(l)):
        needed = s - l[i]
        if needed in _set:
            return [needed, l[i]] # once needed is in the set, it means it's earlier in the list than l[i]. Ensures needed is an el from the list
        else:
            _set.add(l[i])

def main():
    l1 = [1, 4, 8, 7, 3, 15]
    l2 = [1, -2, 3, 0, -6, 1]
    l3 = [20, -13, 40]
    l4 = [1, 2, 3, 4, 1, 0]
    l5 = [10, 5, 2, 3, 7, 5]
    l6 = [4, -2, 3, 3, 4]
    l7 = [0, 2, 0]
    l8 = [5, 9, 13, -3]
    l9 = [1] * 10000000
    l9[len(l9) // 2 - 1] = 6
    l9[len(l9) // 2] = 7
    l9[len(l9) - 2] = 8
    l9[len(l9) - 1] = -3
    l9[0] = 13
    l9[1] = 3
    test.assert_equals(sum_pairs(l1, 8), [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
    test.assert_equals(sum_pairs(l2, -6), [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
    test.assert_equals(sum_pairs(l3, -7), None, "No Match: %s should return None for sum = -7" % l3)
    test.assert_equals(sum_pairs(l4, 2), [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
    test.assert_equals(sum_pairs(l5, 10), [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
    test.assert_equals(sum_pairs(l6, 8), [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
    test.assert_equals(sum_pairs(l7, 0), [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
    test.assert_equals(sum_pairs(l8, 10), [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
    test.assert_equals(sum_pairs(l9, 13), [6, 7], "Ten Million Numbers With Middle Pair: Should terminate with a valid pair output")
    test.assert_equals(sum_pairs(l9, 5), [8, -3], "Ten Million Numbers With Pair At End: Should terminate with a valid pair output")
    test.assert_equals(sum_pairs(l9, 16), [13, 3], "Ten Million Numbers With Pair At Start: Should terminate with a valid pair output")
    test.assert_equals(sum_pairs(l9, 31), None, "Ten Million Numbers With No Match: Should return None in a decent time period")    

if __name__ == "__main__":
    main()

exit()

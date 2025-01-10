"""
KATA DESCRIPTION
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

"""

from sys import exit
import test

def array_diff(a, b):
    dic = {}
    dicIdx = 0

    for i in range (0, len(a)):
        if a[i] not in set(b):
            dic[dicIdx] = a[i]
            dicIdx += 1

    ans = [0] * dicIdx
    for i in range(0, dicIdx):
        ans[i] = dic[i]

    return ans

def main():
    test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
    test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
    test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
    test.assert_equals(array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")    

if __name__ == "__main__":
    main()

exit()


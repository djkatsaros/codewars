"""
You're about to go on a trip around the world! On this trip you're bringing your trusted backpack, that anything fits into. The bad news is that the airline has informed you that your luggage cannot exceed a certain amount of weight.

To make sure you're bringing your most valuable items on this journey you've decided to give all your items a score that represents how valuable this item is to you. It's your job to pack your bag so that you get the most value out of the items that you decide to bring.

Your input will consist of two arrays, one for the scores and one for the weights. Your input will always be valid lists of equal length, so you don't have to worry about verifying your input.

You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.

For instance, given these inputs:

scores = [15, 10, 9, 5]
weights = [1, 5, 3, 4]
capacity = 8

The maximum score will be 29. This number comes from bringing items 1, 3 and 4.

Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.

"""
import test
from sys import exit

def pack_bagpack(scrs, wt, cap):
    n = len(scrs)
    bag = [0 for _ in range(cap + 1)] # only need to update one row in a DP manner.

    for i in range(0, n):
        for w in range(cap, 0, -1):
            if wt[i] <= w: # only update bag if the current weight to update with would not push us over cap
                bag[w] = max( bag[w], bag[w - wt[i]] + scrs[i])

    return bag[-1]

"""
def pack_bagpack(scores, weights, capacity):
    # slicker way to execute same solution
    load = [0] * (capacity + 1)
    for score, weight in zip(scores, weights):
        load = [max(l, weight <= w and load[w - weight] + score)
                for w, l in enumerate(load)]
    return load[-1]
    """

def main():
    test.assert_equals(pack_bagpack([15, 10, 9, 5], [1, 5, 3, 4], 8), 29)
    test.assert_equals(pack_bagpack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10), 60)
    test.assert_equals(pack_bagpack([19,8,6,20,3,16], [8,2,3,10,1,5], 17), 46)
    test.assert_equals(pack_bagpack([100,5,16,18,50], [25,1,3,2,15], 14), 39)
    test.assert_equals(pack_bagpack( [11, 19, 9, 12, 6, 3, 14, 16, 8, 14, 10, 1, 10, 4, 19, 20, 4],  [5, 5, 3, 5, 5, 2, 4, 1, 4, 1, 3, 4, 2, 3, 2, 1, 1], 29), 147)

if __name__ == "__main__":
    main()

exit()

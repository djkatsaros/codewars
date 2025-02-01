"""
Kata Description:
    You're given a square consisting of random numbers, like so:

var square = [
    [1,2,3],
    [4,8,2],
    [1,5,3]];

Your job is to calculate the minimum total cost when moving from the upper left corner to the coordinate given. You're only allowed to move right or down.

In the above example the minimum path would be:

var square = [
    [1,2,3],
    [_,_,2],
    [_,_,3]];

Giving a total of 11. Start and end position are included.

Note: Coordinates are marked as x horizontally and y vertically.
"""
import test
from sys import exit

import numpy as np

def min_path(grid, y, x):
    mincosts = np.zeros((x+1, y+1))
    mincosts[0, 0] = grid[0][0] # initialize

    # base cases
    for i in range(1,x+1):
        mincosts[i, 0] = mincosts[i-1, 0] + grid[i][0]

    for i in range(1,y+1):
        mincosts[0, i] = mincosts[0, i-1] + grid[0][i]

    # DP step
    for i in range(1, x+1):
        for j in range(1, y+1):
            mincosts[i,j] += min(mincosts[i-1, j], mincosts[i, j-1]) + grid[i][j]

    return mincosts[x,y]

def main():
    square = [
    [1, 2, 3, 6, 2, 8, 1],
    [4, 8, 2, 4, 3, 1, 9],
    [1, 5, 3, 7, 9, 3, 1],
    [4, 9, 2, 1, 6, 9, 5],
    [7, 6, 8, 4, 7, 2, 6],
    [2, 1, 6, 2, 4, 8, 7],
    [8, 4, 3, 9, 2, 5, 8]]
    test.assert_equals(min_path(square, 0, 0), 1, 'Failed on small square: [0, 0]')
    test.assert_equals(min_path(square, 0, 1), 5, 'Failed on small square: [0, 1]')
    test.assert_equals(min_path(square, 2, 2), 11, 'Failed on small square: [2, 2]')
    test.assert_equals(min_path(square, 4, 2), 24, 'Failed on small square: [4, 2]')
    test.assert_equals(min_path(square, 6, 6), 39, 'Failed on small square: [6, 6]')
    test.assert_equals(min_path(square, 4, 5), 24, 'Failed on small square: [4, 5]')

if __name__ == "__main__":
    main()

exit()

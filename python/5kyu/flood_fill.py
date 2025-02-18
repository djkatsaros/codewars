"""
Kata Description

Given a 2-dimensional grid and a zero-based (x,y) coordinate, flood-fill the area on the grid containing that coordinate with the given value. Two squares in the grid belong to the same area if they contain the same value and are adjacent either horizontally or vertically, but not diagonally.

See: https://en.wikipedia.org/wiki/Flood_fill
Grid

The grid is represented as a 2-dimensional rectangular array.
Example

A flood fill with 4 at the point (0, 1) of the following array would look like this:

   [[1, 2, 3],     [[1, 4, 3],
    [1, 2, 2],  ->  [1, 4, 4],
    [2, 3, 2]]      [2, 3, 4]]

Note: the input array can be mutated in place."""

import test

def flood_fill(array, r, c, new_value): 
    nbrs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # horizontal moves
    base = array[r][c]                          # base value to flood
    array[r][c]  = new_value                    
    m, n = len(array), len(array[0])
    stack = [(r, c)]                            # init stack of points to change and move fr.
    
    while stack:
        nxt = stack.pop()                       # pop top of stack
        
        for pt in nbrs:                         # iterate through neighrbos, checking each pt is in 
                                                # array and if that point = base floot it and app to stack
            new_pt = (pt[0] + nxt[0], pt[1] + nxt[1])
            if 0 <= new_pt[0] < m and 0 <= new_pt[1] < n:
                if array[new_pt[0]][new_pt[1]] == base:
                    stack.insert(0, new_pt)
                    array[new_pt[0]][new_pt[1]] = new_value
 
    return array

def main():
    expected = [
        [1,4,3],
        [1,4,4],
        [2,3,4]
    ]
    
    actual = [
        [1,2,3],
        [1,2,2],
        [2,3,2]
    ]

    test.assert_equals(flood_fill(actual, 0, 1, 4), expected)

if __name__ == "__main__":
    main()

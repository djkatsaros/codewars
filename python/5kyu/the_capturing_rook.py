"""
Find the minimum distance a rook needs to travel on a n*n chessboard to capture all enemy pawns.

Inputs are the list of pawn positions and the rook starting position. Positions are x,y tuples, with (0,0) being the top-left of the board.

Example:

pawns = [(3, 0), (5, 4), (2, 2), (1, 5)], rook = (2, 3) represents the following board, where each pawn is numbered using its position in the list:

. . . 1 . .
. . . . . .
. . 3 . . .
. . R . . .
. . . . . 2
. 4 . . . .

A rook moves either horizontally or vertically. The distance is the sum of the number of squares traversed as it captures each pawn. In this case, the minimum distance is 15, achieved by capturing the pawns in the order 3->1->2->4.

Constraints:  2 ≤ n ≤ 15; 1 ≤ len(pawns) ≤ n.

This kata was inspired by Rook Count Attack. A related kata is Minimum path in squares

"""
import test
import numpy as np

def totalCost(mask, curr, n, cost, memo):
    """
    bitmasking to find optimal path between destinations a la TSP
    """
    # Base case: if all pawns taken, return 0, as the game ends when all pawns captured.
    if mask == (1 << n) - 1:
        return 0

    # If the value has already been computed, return it
    # from the memo table
    if memo[curr][mask] != -1:
        return memo[curr][mask]

    ans = float('inf')

    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0:

          # If we havent taken pawn, capture pawn i and update the mask
            ans = min(ans, cost[curr][i] +
                      totalCost(mask | (1 << i), i, n, cost, memo))

    # Memoize the result
    memo[curr][mask] = ans
    return ans


def tsp(cost):
    n = len(cost)

    # Initialize memoization table with -1
    memo = [[-1] * (1 << n) for _ in range(n)]

    # Start from city 0, with only city 0 visited initially (mask = 1)
    return totalCost(1, 0, n, cost, memo)

def min_rook_distance(pawns, rook):
    """
    Computes min rook distance to capture all pawns.
    Key:
        Apply TSP with distances being grid distances of R -> pawn for each pawn, then
        pawn1 -> pawn for each pawn, etc., so that the 0th 'city' is then
        the rooks starting position, and each pawn is a city on a grid.
        """
    dists = []

    # collect all pieces
    pieces= [rook]
    for p in pawns:
        pieces += [p]

    # build dists matrix
    for p in pieces:
        rook = p
        d = []
        for r in pieces:
            d += [abs(rook[1] - r[1]) + abs(rook[0] - r[0])]

        dists += [d]
    print(np.array(dists))
    cost = tsp(dists)
    print(cost)
    return cost

def main():
    ## Example from description 
    pawns = [(3, 0), (5, 4), (2, 2), (1, 5)]
    rook = (2, 3)
    path = 'Min path is 3->1->2->4'
    min_distance = 15
    board_size = 6
    test1 = board_size, pawns, rook, min_distance, path 
    
    ## Rectangle
    pawns = [(6, 4), (6, 2), (1, 2), (1, 4)]
    rook = (7, 7)
    path = 'Min path is 1->2->3->4 (or 1->4->3->2)'
    min_distance = 13
    board_size = 8
    test2 = board_size, pawns, rook, min_distance, path 
         
    ## Horizontal line with 'bump'
    pawns = [(6, 3), (2, 3), (3, 4), (5, 3), (1, 3), (4, 3), (0, 3)]
    rook = (0, 0)
    path = 'Min path is 7->5->2->3->6->4->1'
    min_distance = 11
    board_size = 7
    test3 = board_size, pawns, rook, min_distance, path 
    
    ## Pawns ascending, and then descending
    pawns = [(0, 5), (1, 4), (2, 3), (3, 2), (4, 2), (5, 3), (6, 4), (7, 5)]
    rook = (3, 0)
    path = 'Min path is 4->5->6->7->8->1->2->3'
    min_distance = 20
    board_size = 8
    test4 = board_size, pawns, rook, min_distance, path 
    
    tests = [test1, test2, test3, test4]

    for each_test in tests:
        pawns = each_test[1]
        rook = each_test[2]
        test.assert_equals(min_rook_distance(pawns, rook), each_test[3])


if __name__ == "__main__":
    main()

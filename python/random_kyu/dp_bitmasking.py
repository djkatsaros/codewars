"""
dynamic programming and bitmasking used to solve:

    There are N persons and N tasks, each task is to be alloted to a single person. 
    We are also given a matrix cost of size NxN, where cost[i][j] denotes how much person 
    i is going to charge for task j. 
    Assign each task to a person in such a 
    way that the total cost is minimum. Note that each task is to be alloted to 
    a single person, and each person will be alloted only one task.

"""
from sys import maxsize 
import test

def count_set_bits(n):
    """ Returns the nunber of nonzero bits in the binary bit rep of inputed integer"""
    ct = 0 
    while n:
        ct += n & 1
        n >>= 1

    return ct

def assign(cost):
    allMask = (1 << len(cost)) # number of bits we need to represent
    dp = [sys.maxsize] * allMask # initialize so that min ( dp condns ) always less than default
    
    dp[0] = 0 # init with base case
    for mask in range(allMask):
        x = count_set_bits(mask) # number of bits that are set already = the person we are on
        for j in range(len(cost)):
            if mask & (1 << j) == 0:
                dp[ mask | ( << j) ] = min( dp[ mask | (1 << j) ], dp[mask] + cost[x][j])

    return dp[allMask - 1]

def main():
    costs = [ [[1,2,3], [4,54,6], [77,88,99]],
             [[1,1,1], [1,1,1], [1,1,1]] 
             ]
    totals = [85, 3]
    for cost, tot in zip(costs, totals):
        test.assert_equals(assign(cost), tot)

if __name__ == "__main__":
    main()

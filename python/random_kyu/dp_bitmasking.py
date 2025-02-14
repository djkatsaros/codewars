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
    """
    bit masking in a dp tabulation framework to determine best task alottment.
    masks will be numbers whose binary repres a_1 a_2 ... a_k has ith bit a_i = 1 if the ith
    task has been assigned and a_i = 0 if not. 
    """
    allMask = (1 << len(cost)) # binary number with bits set to represent all tasks being done
                               # this means allMask = 0 0 0 ... 0 1 , length = len(cost) = 2^(len(cost)).
    dp = [maxsize] * allMask # initialize so that min ( dp condns ) always less than default
                                 # dp[k] is the (current) cost of assigning tasks to k people
                                 # update with min( current, prev + cost of assigning person k 
                                 # the jth task
    
    dp[0] = 0 # init with base case
    for mask in range(allMask):
        x = count_set_bits(mask) # number of bits that are set already = the person we are on
        for j in range(len(cost)):
            if mask & (1 << j) == 0: # check that jth bit not assigned to a person. this means 
                                     # mask doesn't intersect with 0 0 ... 0 1 0 ... 0
                                     #  `                                   jth 
                dp[ mask | (1 << j) ] = min( dp[ mask | (1 << j) ], dp[mask] + cost[x][j])
                # mask | (1 << j) is setting jth bit of mask to be 1 -> assigning jth task
                #   Assigning this task brings mask to (mask + (1 << j))th person, updating
                #   total cost of assigning tasks to mask + (1 << j) people.
                # mask + jth bit entry of dp  being assigned 
                #   = min(  mask | (1 << j), mask + cost[x][j] )
                #   = min ( mask after setting jth bit, mask + cost of xth person doing task j)
                print(mask | (1 << j) , dp[mask | (1 << j)], dp[mask] + cost[x][j] )
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

"""
Kata Description:
    Create a function that returns an array containing the first l numbers from the nth diagonal of Pascal's triangle.

n = 0 should generate the first diagonal of the triangle (the ones).
The first number in each diagonal should be 1.
If l = 0, return an empty array.
Both n and l will be non-negative integers in all test cases.
    """

import test
from sys import exit
from math import factorial 

def n_choose_k(n,k):
    """Binomial coefficient"""
    return factorial(n) // (factorial(k) * factorial(n-k))    
    
def generate_diagonal(n, l):
    """The diagonals are (n choose k) starting from n choose 0, then (n+1) choose 1,
    then (n+2) choose 2 etc. """
    if n == 0:
        return [1]*l
    
    out = []
    k = 0 
    for idx in range(l):        
        out += [n_choose_k(n,k)] #n choose k
        n += 1
        k += 1
    
    return out

def main():
    test.assert_equals(generate_diagonal(2, 5),[1, 3, 6, 10, 15])
    test.assert_equals(generate_diagonal(1, 10),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test.assert_equals(generate_diagonal(3, 7),[1, 4, 10, 20, 35, 56, 84])

if __name__ == "__main__":
    main()

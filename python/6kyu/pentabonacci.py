"""
Description:
    We have the following sequence:

f(0) = 0
f(1) = 1
f(2) = 1
f(3) = 2
f(4) = 4;
f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5);

Your task is to give the number of total values for the odd terms of the sequence up to the n-th term (included). (The number n (of n-th term) will be given as a positive integer)

The values 1 (one) is the only that is duplicated in the sequence and should be counted only once.

E.g.

count_odd_pentaFib(5) -----> 1 # because the terms up to 5 are: 0, 1, 1, 2, 4, 8 (only 1 is odd and counted once)

Other examples:

 count_odd_pentaFib(10) ------> 3 #because the odds terms are: [1, 1, 31, 61] (three different values)

count_odd_pentaFib(15) ------> 5 # beacause the odd terms are: [1, 1, 31, 61, 1793, 3525] (five different values)

Good luck !!
"""

import test
import numpy as np

def count_odd_pentaFib(n):

    pentaFib = [0,1,1,2,4] # initialize penta Fib seq.
    if n <= 2:
        return pentaFib[n]

    dp = [0] * (n+1)

    for i in range(0, min(n,4) + 1):
        dp[i] = pentaFib[i]

    if n >= 5:
        for i in range(5, n+1):
            dp[i] = sum(dp[i-5 : i])

    #create indicator array. dp[indic] = odd values.
    indic = np.array(list(map(lambda x: x % 2 == 1, dp)))

    return len(set(np.array(dp)[indic]))

def main():
    test.assert_equals(count_odd_pentaFib(5), 1)
    test.assert_equals(count_odd_pentaFib(10), 3)
    test.assert_equals(count_odd_pentaFib(15), 5)
    test.assert_equals(count_odd_pentaFib(45), 15)
    test.assert_equals(count_odd_pentaFib(68), 23)
    test.assert_equals(count_odd_pentaFib(0),0)
    test.assert_equals(count_odd_pentaFib(1),1)
    test.assert_equals(count_odd_pentaFib(2),1)

if __name__ == "__main__":
    main()

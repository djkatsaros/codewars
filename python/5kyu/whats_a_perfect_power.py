"""
Kata Description:
    A perfect power is a classification of positive integers:

    In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.

Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with mk = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.

Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.
Examples

isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None

"""

## solve is using bisection method on the interval [2, 2^k] such that 2^k >= n. 
# iteratively increase the exponent by 1 and repeat bisection method until we find n.
# everytime we divide the interval in half, check the midpoint raised to current exponent 
# until mid ** e is as close to n as possible -> see basic real analysis to see why this works.
# 
#
# uncomment print stmts for a more verbose and transparent run 

import test
from random import random, randrange
from math import log, floor

def isPP(n):
    """bisection method"""
    e = 2
    while True:
        if 2 ** e > n:
            return None # smallest perfect power is 4, 2^2  = 4. Also exits loop if we surpass n
        left = 2
        right = 2
        while right ** e <= n: # find upper limit to the interval: if 2 ** e > n, then a ** b > n for any a >= 2 and b >= e
            right *= 2
        #print(left,right)
        while right - left > 1: # we will progressively make left and right merge together -> left the desired root if e is the right exponent
            mid = (left + right) // 2
            if mid ** e <= n:
                left = mid # midpoint between L and R is less than n at the exponent e. n is in the right interval
            else:
                right = mid # n is in the left interval
            #print(left, right)

        if left ** e == n:
            #print("root, exponent are: {}, {}".format(left, e))
            return [left, e]
        e += 1

def main():
    print("should work for some examples:")
    test.assert_equals(isPP(4), [2,2], "4 = 2^2")
    test.assert_equals(isPP(9), [3,2], "9 = 3^2")
    test.assert_equals(isPP(5), None, "5 isn't a perfect power")

    print("should work for the first perfect powers")
    pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
    for item in pp:
        test.expect(isPP(item) != None, "the perfect power "+str(item)+" wasn't recognized as one")
    
    print("should_work_for_random_perfect_powers")
    for i in range(100):
        m = 2 + floor(random() * 255)
        k = 2 + floor(random() * log(268435455) / log(m))
        l = m**k
        r = isPP(l)
        if r==None:
            test.expect(r != None, str(l) + " is a perfect power")
            break
        else:
            test.assert_equals(r[0]**r[1], l, "your pair (" + str(r[0]) + ", "+ str(r[1])+ ") doesn't work for "+ str(l))
            #break

if __name__ == "__main__":
    main()

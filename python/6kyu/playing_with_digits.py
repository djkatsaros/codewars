"""
Kata Description:

Some numbers have funny properties. For example:

    89 --> 8¹ + 9² = 89 * 1
    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :
(ap+bp+1+cp+2+dp+3+...)=n∗k(a^p + b^{p + 1} + c^{p + 2} + d^{p + 3} + ...) = n * k(ap+bp+1+cp+2+dp+3+...)=n∗k

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers.
"""

import test
from sys import exit

def dig_pow(n, p):
    s = 0
    for i in list(str(n)):
        print(type(int(i)),int(i))
        s += int(i)**p
        p += 1

    if s % n == 0:
        return s // n
    else:
        return -1

def main():
    test.assert_equals(dig_pow(89, 1), 1)
    test.assert_equals(dig_pow(92, 1), -1)
    test.assert_equals(dig_pow(46288, 3), 51)
    test.assert_equals(dig_pow(41, 5), 25)
    test.assert_equals(dig_pow(114, 3), 9)
    test.assert_equals(dig_pow(8, 3), 64)

if __name__ == "__main__":
    main()

exit()

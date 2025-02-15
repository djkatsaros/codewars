"""
Kata Description:
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

Example:
countOnes 4 7 should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.

WARNING: Segment may contain billion elements, to pass this kata, your solution cannot iterate through all numbers in the segment!

"""


"""
KEY IDEA:

Each number has a particular number of digits in its binary representation.
There are sets of numbers with the same number of digits in their binary representation.
For example there is a set of 4-digit-numbers: 8,9,10,11,12,13,14,15.

num | binary representation
  8 | 1 0 0 0
  9 | 1 0 0 1
 10 | 1 0 1 0
 11 | 1 0 1 1
 12 | 1 1 0 0
 13 | 1 1 0 1
 14 | 1 1 1 0
 15 | 1 1 1 1

That kind of sets of n-digit numbers we will call 'blocks'.
For whole blocks we can easily calculate sum of ones with the formula 

2^(n-1) * (1 + 0.5*(n-1))

But 'left' and 'right' digits can be somewhere inside of their blocks, so we have to sum only part of ones in block.

For example, in case of range <10, 35> we have to split our calculation in 3 parts:
1) Sum of the incomplete 4-digit-block, which contains number 10.
Number 10 splits that block on two parts and we sum ones only from second part (for numbers 10-15).
2) Sum of 5-digit-block (ones in numbers: 16-31)
3) Sum of the incomplete 6-digit-block, which contains number 35.
Number 35 splits that block on two parts and we sum ones only from first part (for numbers 32-35).

:return: sum of ones in binary representation of all numbers in range <left, right>
"""

import test

def count_1s_from_0_to(n: int) -> int:
    """ essentially the formula in the above but in bit notation """
    cnt = 0
    while n:
        b = n.bit_length() - 1  # number of bits in bin rep of n minus 1
        m = 1 << b              # 2 ^ b
        cnt += b * (m >> 1) + n - m + 1 # (bits - 1) * 2^(b - 1)
        n ^= m
    return cnt


def bindig(number):
    ans=0
    g= bin(number)[2:][::-1]
    
    for i in range(len(g)):
        if g[i] == '1':
            if i == len(g) - 1:
                ans += 1 + ((2**(i - 1)) * i)
            else: 
                ans += 1 + (2**(i - 1)) * i + (g[i + 1:].count('1')) * (2**i)
    return ans

def count_ones(left, right):
    return bindig(right)-bindig(left-1)
    #return count_1s_from_0_to(right) - count_1s_from_0_to(left - 1)

def main():
    test.assert_equals(count_ones(5,7), 7)
    test.assert_equals(count_ones(12,29), 51)

if __name__ == "__main__":
    main()

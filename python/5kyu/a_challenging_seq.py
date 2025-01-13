"""
Kata Description.
Each composed integer may have a prime factorization. If n is the integer, it will be:

[source: imgur.com]

and k1, k2, k3....., kn are the exponents corresponding to each prime in the factorization.

The radical of n, Rad(n), will be the product of all the prime factors of the number, (without the exponents), so:

Rad(n) = p1 . p2 . p3 .....pn

Let's see an example for a number, if n = 172800

its prime factorization will be

n = 2^8 . 3^3 . 5^2,

Rad(172800) = 2 . 3 . 5 = 30

Many numbers, smaller than 172800, may have a radical considerably higher than 30, for example:

Rad(9305) = 5 . 1861 = 9305

Primes are a particular case, the value of its radical coincides with the value of the prime itself

Rad(31) = 31

Rad(57) = 57

To number 1 it's assigned, Rad(1) = 1

Let's see the comparison between numbers and radicals for the first 10 numbers

   n       Prime Descomposition    Prime Factors     Radical(n)
   1                                                         1
   2               2                       2                 2
   3               3                       3                 3
   4              2, 2                     2                 2
   5               5                       5                 5
   6              2, 3                    2, 3               6
   7               7                       7                 7
   8              2, 2, 2                  2                 2
   9              3, 3                     3                 3
  10              2, 5                    2, 5               10

The list above may be sorted by the value of the radicals and the order changes having another sequence. We add a new column that gives the ordinal number of different values

k- Term        n       Radical(n)
1              1            1
2              2            2
3              4            2
4              8            2
5              3            3
6              9            3
7              5            5
8              6            6
9              7            7
10            10            10

We have some numbers that have the same value for its radical, the smaller numbers are selected to go first. For example, n = 2, 4, 8 have Radical(n) = 2, these numbers should be ordered by their own value.

Create a function hash_radSeq() that receives two arguments:

    nMax is the upper bound such that all values of n are in the interval (1, nMax) (1 <= n <= nMax)

    the number k, which is the ordinal number of a certain term in a sequence sorted by the values of the radicals

    the function should ouput the value of n, for the corresponding ordinal number k (k-th), in a sequence sorted bby the values of Rad(n) Let's see some examples:

    hash_radSeq(10, 4) ------> 8
    hash_radSeq(10, 6) ------> 9
    hash_radSeq(10, 9) ------> 7

If we increase of the number of nMax to 20, the sequence changes

hash_radSeq(20, 4) ------> 8
hash_radSeq(20, 6) ------> 3
hash_radSeq(20, 9) ------> 6

(Your code will be tested for values of nMax up to 60000 and values of k up to 11000, so try to think in some data structure, useful for fast hashing)

Happy coding!!

"""


def hash_rad_seq(n_max, k):
    """Due to https://www.codewars.com/users/Shane%20Audrey%20R.%20Tagpuno
    uses Sieve of Eratosthenes to compute radicals:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    # Step 1: Initialize an array to hold the radical values.
    radicals = [1] * (n_max + 1)

    # Step 2: Use a modified Sieve of Eratosthenes to calculate radicals.
    for i in range(2, n_max + 1):
        if radicals[i] == 1:  # i is a prime number
            for j in range(i, n_max + 1, i):
                radicals[j] *= i

    # Step 3: Create a list of tuples (Rad(n), n) for all numbers in the range.
    rad_list = [(radicals[i], i) for i in range(1, n_max + 1)]

    # Step 4: Sort by Rad(n) first, and by n second if radicals are equal.
    rad_list.sort()

    # Step 5: Return the n value for the k-th position (1-indexed).
    return rad_list[k - 1][1]

def main():
    # Test cases
    print(hash_rad_seq(10, 4))  # Output: 8
    print(hash_rad_seq(10, 6))  # Output: 9
    print(hash_rad_seq(10, 9))  # Output: 7
    print(hash_rad_seq(20, 4))  # Output: 8
    print(hash_rad_seq(20, 6))  # Output: 3
    print(hash_rad_seq(20, 9))  # Output: 6

if __name__ == "__main__":
    main()

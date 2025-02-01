"""
Kata Description:
    If you reverse the word "emirp" you will have the word "prime". That idea is related with the purpose of this kata: we should select all the primes that when reversed are a different prime (so palindromic primes should be discarded).

For example: 13, 17 are prime numbers and the reversed respectively are 31, 71 which are also primes, so 13 and 17 are "emirps". But primes 757, 787, 797 are palindromic primes, meaning that the reversed number is the same as the original, so they are not considered as "emirps" and should be discarded.

The emirps sequence is registered in OEIS as A006567
Your task

Create a function that receives one argument n, as an upper limit, and the return the following array:

[number_of_emirps_below_n, largest_emirp_below_n, sum_of_emirps_below_n]
Examples

find_emirp(10)
[0, 0, 0] ''' no emirps below 10 '''

find_emirp(50)
[4, 37, 98] ''' there are 4 emirps below 50: 13, 17, 31, 37; largest = 37; sum = 98 '''

find_emirp(100)
[8, 97, 418] ''' there are 8 emirps below 100: 13, 17, 31, 37, 71, 73, 79, 97; largest = 97; sum = 418 '''

Happy coding!!

Advise: Do not use a primality test. It will make your code very slow. Create a set of primes using a prime generator or a range of primes producer. Remember that search in a set is faster that in a sorted list or array

#### Extra comment

    This Kata sucks. Most of the difficulty is just computing a sufficient number of 
    primes efficiently enough, and even though the description advises avoiding a 
    primality test, you can pass using one. Not an interesting puzzle.

####
"""

from sys import exit
import test

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num+1)
    for num in range(2, int(max_num**0.5) + 1):
        if is_prime[num]:
            for i in range(num*num, max_num+1, num):
                is_prime[i] = False
    return [num for num in range(2, max_num+1) if is_prime[num]]

def is_prime(n):
    if n % 2 == 0 or n < 3:
        return n == 2
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True


def find_emirp(n):
    ps = sieve_of_eratosthenes(n)
    emirps = [i for i in ps if is_prime(int(str(i)[::-1])) and i != int(str(i)[::-1])]

    if is_prime(n) and is_prime(int(str(n)[::-1])) and n != int(str(n)[::-1]):
        emirps += [n]

    if emirps:
        return [len(emirps), max(emirps), sum(emirps)]
    else:
        return [0,0,0]

def main():
    nums = [50, 100, 200, 500, 750, 1000, 3000, 7000, 10000, 15000, 20000]

    results = [[4, 37, 98], [8, 97, 418], [15, 199, 1489], [20, 389, 3232], [25, 743, 6857], [36, 991, 16788], 
               [96, 1979, 103268], [147, 3929, 278175], [240, 9967, 1076242], [446, 14957, 3661772], [627, 19973, 6827225]]
              
    for num, exp in zip(nums, results):
        test.assert_equals(find_emirp(num), exp)

if __name__ == "__main__":
    main()

exit()

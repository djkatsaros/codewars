"""
KATA DESCRIPTION
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

alternative text
Hint:

See Fibonacci sequence
Ref:

http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216

"""

from sys import exit
import test

def perimeter(n):
    """ perimeter of squares is always the sum of the n+1 fib numbers times 4"""
    _fib = 1 # first fib number
    tot = 1 # initialize the total to 1 to save the step in the for loop.
    a = 0
    b = 0

    for i in range(1,n+1):
        a = b
        b = _fib
        _fib = a + b
        tot += _fib

    return 4 * tot

def main():
    test.assert_equals(perimeter(0), 4)
    test.assert_equals(perimeter(5), 80)
    test.assert_equals(perimeter(7), 216)
    test.assert_equals(perimeter(20), 114624)
    test.assert_equals(perimeter(30), 14098308)
    test.assert_equals(perimeter(100), 6002082144827584333104)
    test.assert_equals(perimeter(500), 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504)


if __name__ == "__main__":
    main()

exit()


"""
Kata Description:
Imagine a honeycomb - a field of hexagonal cells with side N. There is a bee in the top left cell A. In one move it can crawl one cell down, one cell down-right or one cell up-right (the bee does not crawl up or left).

Write a function that outputs the number of ways the bee can crawl from cell A to the opposite cell B.

Input data:

The function receives a single number N - the size of the hexagonal field 2 ≤ N ≤ 200.

Output data:

The function should output a single integer - the number of ways.
    """
import test

def the_bee(n):
    
    cells = [0] * (2*n + 1)
    cells[n] = 1
    
    for i in range(1, 4*n-2):
        for j in range(i%2 + 1, 2*n, 2):
            cells[j-1] += cells[j]
            cells[j+1] += cells[j]
    
    return cells[n]

def main():
    test.assert_equals(the_bee(2), 11)
    test.assert_equals(the_bee(3), 291)
    test.assert_equals(the_bee(5), 259123)
    test.assert_equals(the_bee(20), 11419120154603538332020717795)
    test.assert_equals(the_bee(33), 706829476133138423874525925298446150375545319299)
    test.assert_equals(the_bee(50), 61068096560504518254246449553519425203436341865056944755649047832571626123)

if __name__ == "__main__":
    main()

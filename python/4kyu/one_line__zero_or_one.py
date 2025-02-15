"""
Task

You are given an odd integer n and a two-dimensional array s, which contains n equal-sized arrays of 0s and 1s.

Return an array of the same length as the elements of n, such that its ith element is the one that appears most frequently at the ith position of s' elements.
Code Limit

Less than 55 characters.
Example

For n = 3, s = [[1,1,0], [1,0,0], [0,1,1]],

the output should be [1,1,0]

1st  2nd  3rd
 1    1    0
 1    0    0
 0    1    1


At the 1st position
there're two 1s and one 0,
so in the 1st element of the resulting array is 1.

At the 2nd position
there're two 1s and one 0,
so in the 2nd element of the resulting array is 1.

At the 3rd position
there're two 0s and one 1,
so in the 3rd element of the resulting array is 0.

"""

import test

zero_or_one=lambda n,s:[sum(r)>n/2 for r in zip(*s)]
soln_str = "zero_or_one=lambda n,s:[sum(r)>n/2 for r in zip(*s)]"

def main():
    sample_test_cases = [

#    n     s              result

    (1,  [[1,1,0,1]],     [1, 1, 0, 1]),

    (3,  [[1,0,1,0,1],
          [1,0,1,0,1],
          [0,1,0,1,0]],   [1, 0, 1, 0, 1]),

    (3,  [[1,0,1,0,1],
          [1,1,1,0,1],
          [0,1,1,1,0]],   [1, 1, 1, 0, 1]),

    (5,  [[1,0,0,0,0],
          [0,1,0,0,0],
          [0,0,1,0,0],
          [0,0,0,1,0],
          [0,0,0,0,1]],   [0, 0, 0, 0, 0]),
]

    print(f"Solution length is {len(soln_str)}, which needs to be less than 55. This is {len(soln_str)<=55}")
    for n, s, expected in sample_test_cases:
        test.assert_equals(zero_or_one(n, s), expected)

if __name__ == "__main__":
    main()

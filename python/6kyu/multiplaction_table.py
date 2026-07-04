"""
    Description:
    your task is to create an NxN multiplication table of size provided in parameter.
    Example: for given size 3,
    1 2 3
    2 4 6
    3 6 9
"""
import test
from sys import exit

def multiplication_table(size):
    out = []
    out.append([i for i in range(1, size + 1) ])
    for n in out[0][1:]:
        out.append([n * i for i in range(1, len(out[0]) + 1)])
    #print(out)
    return out

def main():
    # test cases
    test.assert_equals(multiplication_table(1), [[1]])
    test.assert_equals(multiplication_table(2), [[1, 2], [2, 4]])
    test.assert_equals(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    test.assert_equals(multiplication_table(4), [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
    test.assert_equals(multiplication_table(5), [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]])
    

if __name__ == "__main__":
    main()
exit()


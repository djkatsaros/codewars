"""
KATA DESCRIPTION
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

import test
from sys import exit

import numpy as np

def _rotation(arr):   
    """Visually, executes a counterclockwise rotation of inputed array:
                    ---->      [[6,9],  
        [[4,5,6],  becomes      [5,8],
         [7,8,9]]   ---->       [4,7]]  """
    return arr[0::,-1::-1].transpose()


def snail(arr):
    arr = np.array(arr) # input not passed in as an array.
    a = arr[0,::] # first row. 
    while arr.shape[0] > 1:
        arr = _rotation(arr[1::]) # rotate everything but the first row. 
        a = np.append(a, arr[0,::]) # append first row of the rotated array. 
    return list(a)  

def main():
    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    test.assert_equals(snail(array), expected)


    array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
    expected = [1,2,3,4,5,6,7,8,9]
    test.assert_equals(snail(array), expected)

if __name__ == "__main__":
    main()

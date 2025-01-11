"""
KATA DESCRIPTION
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""

import test
from sys import exit
import numpy as np

def same_structure_as(original,other):
    # First, check basic criteria needed for the nesting structures to be same: length and type.
    if type(original) == type(other):
        if len(original) == len(other):
            # boolean value
            same_struct=True
            for i in range(len(original)):
                # use numpy shape method on each el.
                if np.array(original[i]).shape != np.array(other[i]).shape:
                    same_struct=False
            return same_struct

    else:
        return False

def main():
    test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
    test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")

if __name__ == "__main__":
    main()

exit()

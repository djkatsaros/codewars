"""
Kata Description:
    Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

Rules for validation

    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

"""

import test
import numpy as np

class Sudoku(object):

    def __init__(self, data):
        """Initialize the object. All information comes from the data"""
        self.board = data                                   # set the board 
        self.size = len(data)                               # size of the board
        self.little_size = int(len(data)**(1 / 2))          # size of small squares
        self.tot = sum([i+1 for i in range(len(data))])     # total we need each row and col to sum to 
        self.nums = set([i+1 for i in range(len(data))])    # set of numbers we need each row, col, and small square to contain
    
    def __str__(self):
        """Prints info about the board"""
        return f"The sudoku board is {self.board}. \n It is inteded to have size {self.size} by {self.size}. \n We will check that the board is of valid shape, that each row and column has total equal to {self.tot}, that each sqrt{self.size} by sqrt{self.size} small square contains each number from 1 to {self.size}, and that all entires are of type int.\n"
    
    def is_valid(self):
        """Validataes the board.
        First: check the types in each row are all inttegers and the right length
        Second: Check column sums.
        Third: Check row sums.
        Fourth: Check contents of small squres."""
        
        print(self)

        for r in self.board:
            if list(map(type, r)) != [int] * self.size:
                return False
        
        valid = True
        for c in zip(*self.board):
            #print(sum(c) == self.tot)
            valid = (sum(c) == self.tot)
            if not valid:
                return False
                
        for r in  self.board:
            #print(sum(r) == self.tot)
            valid = (sum(r) == self.tot)
            if not valid:
                return False
        
        npBoard = np.array(self.board)
        for i in range(0, self.size, self.little_size):
            for j in range(0, self.size, self.little_size): 
                if set(npBoard[i:i+self.little_size, j:j+self.little_size].reshape(1,self.size)[0]) != self.nums:
                    return False 
        
        return valid
        
def main():
        # Valid Sudoku
    goodSudoku1 = Sudoku([
      [7,8,4, 1,5,9, 3,2,6],
      [5,3,9, 6,7,2, 8,4,1],
      [6,1,2, 4,3,8, 7,5,9],

      [9,2,8, 7,1,5, 4,6,3],
      [3,5,7, 8,4,6, 1,9,2],
      [4,6,1, 9,2,3, 5,8,7],

      [8,7,6, 3,9,4, 2,1,5],
      [2,4,3, 5,6,1, 9,7,8],
      [1,9,5, 2,8,7, 6,3,4]
    ])

    goodSudoku2 = Sudoku([
      [1,4, 2,3],
      [3,2, 4,1],

      [4,1, 3,2],
      [2,3, 1,4]
    ])

    # Invalid Sudoku
    badSudoku1 = Sudoku([
      [0,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],

      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],

      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9]
    ])

    badSudoku2 = Sudoku([
      [1,2,3,4,5],
      [1,2,3,4],
      [1,2,3,4],
      [1]
    ])
    test.assert_equals(goodSudoku1.is_valid(), True, 'Testing valid 9x9')
    test.assert_equals(goodSudoku2.is_valid(), True, 'Testing valid 4x4')
    test.assert_equals(badSudoku1.is_valid(), False, 'Values in wrong order')
    test.assert_equals(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')

if __name__ == "__main__":
    main()


"""
Kata Description:

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

Note: your solution must not modify the input list.
"""

import test
from collections import defaultdict

def score(dice):
    die_ct = defaultdict(int)

    for d in dice:
        die_ct[d] += 1

    score = 0
    for t in (zip(die_ct.keys(), die_ct.values())):
        match t[0]:
            case 1:
                match t[1]:
                    case 1 | 2:
                        score += t[1] * 100
                    case 3 | 4 | 5:
                        score += 1000 + 100 * (t[1] - 3)
            case 5:
                match t[1]:
                    case 1 | 2:
                        score += t[1] * 50
                    case 3 | 4 | 5:
                        score += 500 + 50 * (t[1] - 3)
            case 2:
                match t[1]:
                    case 3 | 4 | 5:
                        score += 200
            case 3:
                match t[1]:
                    case 3 | 4 | 5 :
                        score += 300
            case 4:
                match t[1]:
                    case 3 | 4 | 5:
                        score += 400
            case 6:
                match t[1]:
                    case 3 | 4 | 5:
                        score += 600

    return score

def main():
    test.assert_equals( score( [5, 1, 3, 4, 1] ),  250)
    test.assert_equals( score( [1, 1, 1, 3, 1] ), 1100)
    test.assert_equals( score( [2, 3, 4, 6, 2] ),    0)
    test.assert_equals( score( [4, 4, 4, 3, 3] ),  400)
    test.assert_equals( score( [2, 4, 4, 5, 4] ),  450)

if __name__ == "__main__":
    main()

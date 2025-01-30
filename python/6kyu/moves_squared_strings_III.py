"""KATA DESCRIPTION:

    You are given a string of n lines, each substring being n characters long: For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study some transformations of this square of strings.

Let's now transform this string!

    Symmetry with respect to the main diagonal: diag_1_sym (or diag1Sym or diag-1-sym)

    diag_1_sym(s) => "aeim\nbfjn\ncgko\ndhlp"

    Clockwise rotation 90 degrees: rot_90_clock (or rot90Clock or rot-90-clock)

    rot_90_clock(s) => "miea\nnjfb\nokgc\nplhd"

    selfie_and_diag1(s) (or selfieAndDiag1 or selfie-and-diag1) It is initial string + string obtained by symmetry with respect to the main diagonal.

    s = "abcd\nefgh\nijkl\nmnop" --> 
    "abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"

    or printed for the last:

selfie_and_diag1
abcd|aeim
efgh|bfjn
ijkl|cgko 
mnop|dhlp

Task:

    Write these functions diag_1_sym, rot_90_clock, selfie_and_diag1

and

    high-order function oper(fct, s) where

    fct is the function of one variable f to apply to the string s (fct will be one of diag_1_sym, rot_90_clock, selfie_and_diag1)

Examples:

s = "abcd\nefgh\nijkl\nmnop"
oper(diag_1_sym, s) => "aeim\nbfjn\ncgko\ndhlp"
oper(rot_90_clock, s) => "miea\nnjfb\nokgc\nplhd"
oper(selfie_and_diag1, s) => "abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"
"""

import numpy as np
import test
from sys import exit

def matrix_str(strng):
    l = strng.split('\n')
    return [list(s) for s in l]

def rot_90_clock(strng):
    arr = np.array(matrix_str(strng))
    arr = np.rot90(arr, 3)

    out = ""
    for s in arr:
        out += "".join(s) + "\n"

    return out[:-1]

def diag_1_sym(strng):
    arr = matrix_str(strng)
    for i in range(0, len(arr[0])):
        for j in range(i, len(arr)):
            #print(arr[i][j])
            tmp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = tmp

    out = ""
    for s in arr:
        out += "".join(s) + "\n"

    return out[:-1]


def selfie_and_diag1(strng):
    out = ""
    right = diag_1_sym(strng)
    for (L, R) in zip(strng.split("\n"), right.split("\n")):
        out += L + "|" + R + "\n"

    return out[:-1]

def oper(fct, s):
    return fct(s)

def testing(actual, expected):
    test.assert_equals(actual, expected)

def main():
    testing(oper(rot_90_clock, "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb"),
            "Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle")
    testing(oper(diag_1_sym, "wuUyPC\neNHWxw\nehifmi\ntBTlFI\nvWNpdv\nIFkGjZ"),
            "weetvI\nuNhBWF\nUHiTNk\nyWflpG\nPxmFdj\nCwiIvZ")
    testing(oper(selfie_and_diag1, "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg"),
            "NJVGhr|NMtsrz\nMObsvw|JOPotj\ntPhCtl|VbhEQl\nsoEnhi|GsCnRi\nrtQRLK|hvthLW\nzjliWg|rwliKg")


if __name__ == "__main__":
    main()

exit()

"""
KATA DESCRIPTION
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
Example:

"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      ->  400
"XC"      ->   90
"XL"      ->   40
"I"       ->    1

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

"""
import test
from sys import exit

def solution(roman : str) -> int:

    key = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    res = 0
    i = 0
    while i < len(roman):
        s1 = key[roman[i]]

        if i < len(roman) - 1:
            s2 = key[roman[i+1]]

            if s1 >= s2:
                res += s1
                i += 1
            else:
                res += s2 - s1
                i += 2
        else:
            res += s1
            i += 1
        print(i, res)


    return res
def do_test(roman : str, n : int):
    actual = solution(roman)
    test.assert_equals(actual, n, f'for roman {roman}')

def main():
    do_test('MMMCMXCIX',       3999)
    do_test('MMMDCCCLXXXVIII', 3888)
    do_test('MM',              2000)
    do_test('MDCLXVI',         1666)
    do_test('M' ,              1000)
    do_test('CD',               400)
    do_test('XC',                90)
    do_test('XL',                40)
    do_test('I' ,                 1)    

if __name__ == "__main__":
    main()

exit()

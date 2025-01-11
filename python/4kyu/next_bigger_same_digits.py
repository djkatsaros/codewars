"""
KATA DESCRIPTION
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
"""

import test
from sys import exit

def _smallest(l):
    """ takes in a list corrg to a integer. returns a list corrg to the smallest integer
    having the same digits"""
    if len(l) == 1:
        return l
    else:
        new = []
        while l != []:
            new.append(min(l) )
            l.remove(min(l))
        return new

def next_bigger(n):
    """ Calculates the next larger integer with the same digit as the input"""
    s = list(str(n))
    found=False
    for i in  range(len(s)-1,0,-1):
        if s[i-1] < s[i]:
            temp = s[i-1]
            m = min([el for el in s[i::] if el > temp ] )
            temp2 = s[i::].index(m)+i
            s[i-1] = m
            if type(temp2) == list:
                s[temp2[0]] = temp
            else:
                s[temp2] = temp
            s[i::] = _smallest(s[i::])
            found =True
            return int("".join(s))
    if found == False:
        return -1

def main():
    test.assert_equals(next_bigger(  12),   21)
    test.assert_equals(next_bigger(  21),   -1)
    test.assert_equals(next_bigger( 513),  531)
    test.assert_equals(next_bigger(2017), 2071)
    test.assert_equals(next_bigger( 414),  441)
    test.assert_equals(next_bigger( 144),  414)

if __name__ == "__main__":
    main()

exit()

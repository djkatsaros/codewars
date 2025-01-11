"""
KATA DESCRIPTION
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

"""

from sys import exit
import test

import string
from codecs import encode as _dont_use_this_

def rot13(message):
    mess = []
    rang =list( range(0,26)) + list(range(0,26))
    letts = list(string.ascii_lowercase ) + list(string.ascii_uppercase)
    dletters = dict(zip(letts, rang))
    dlower_rev = dict(zip( range(0,26), list(string.ascii_lowercase)))
    dupper_rev = dict(zip( range(0,26), list(string.ascii_uppercase)))
    for char in list(message):
        try:
            if char.islower():
                mess.append(dlower_rev[( dletters[ char] + 13) % 26])
            elif char.isupper():
                mess.append(dupper_rev[( dletters[ char] + 13) % 26])
            else:
                dletters[char]
        except KeyError:
            mess.append(char)

    s = ''.join(mess)
    return s

def main():
    test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
    test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
    test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')    
    
if __name__ == "__main__":
    main()

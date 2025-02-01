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

from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers

def rot13(message):
    mess = []
    keyholes = range(0,26)
    lkeyholes = list(keyholes)
    lowers_ = list(lowers) 
    uppers_ = list(uppers)
    
    rang = 2 * lkeyholes 
    letts = lowers_ + uppers_
    dletters = dict(zip(letts, rang))
    dlower_rev = dict(zip( keyholes, lowers_ ))
    dupper_rev = dict(zip( keyholes, uppers_ ))
    
    for char in list(message):
        try:
            if char.islower():
                mess.append(dlower_rev[( dletters[ char] + 13) % 26]) 
            elif char.isupper():
                mess.append(dupper_rev[( dletters[ char] + 13) % 26]) 
            else:
                mess.append(dletters[char])
        except KeyError:
            mess.append(char)  
            
    s = ''.join(mess)
    
    return s 

def main():
    test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
    test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
    test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')    
    test.assert_equals(rot13("EBG13 rknzcyr."), "ROT13 example.")
    test.assert_equals(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."), "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
    test.assert_equals(rot13("123"), "123")
    test.assert_equals(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"), "This is actually the first kata I ever made. Thanks for finishing it! :)")
    test.assert_equals(rot13("@[`{"), "@[`{")

if __name__ == "__main__":
    main()

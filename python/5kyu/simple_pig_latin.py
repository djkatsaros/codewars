"""
Kata Description:
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import test
from sys import exit

def pig_it(text):
    #EZ
    out = []
    for s in text.split():
        if s in [',', '.', '?', '!']:
            out.append(s)
        else:
            out.append(s[1:len(s)+1] + s[0] +'ay')

    return " ".join(out)

def main():
    test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
    test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')

if __name__ == "__main__":
    main()

exit()

"""
Kata Description
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

    Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with either ) or D

No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
Example

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note

In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

"""

import test
from sys import exit

def count_smileys(arr):
    count = 0
    mouths=[')','D']
    eyes=[':',';']
    noses=['-','~']
    for smilee in arr:
        if smilee !=[] and smilee[0] in eyes and smilee[-1] in mouths:
            if len(smilee)==2:
                count +=1
            else:
                if smilee[1] in noses:
                    count += 1

    return count

def main():
    test.assert_equals(count_smileys([]), 0)
    test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
    test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
    test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)    

if __name__ == "__main__":
    main()

exit()

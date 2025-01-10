"""
KATA DESCRIPTION
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""


"""

from sys import exit
import test

def clean_string(s):
    out = []
    for c in s:
        if c == '#':
            if out != []:
                out.pop()
        else:
            out.append(c)
    return ''.join(out)

def main():
    test.assert_equals(clean_string('abc#d##c'), "ac")
    test.assert_equals(clean_string('abc####d##c#'), "" )
    test.assert_equals(clean_string("#######"), "" )
    test.assert_equals(clean_string(""), "" )

if __name__ == "__main__":
    main()

exit()

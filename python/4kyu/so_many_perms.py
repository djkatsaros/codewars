"""
Kata Description:
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

Note: The order of the permutations doesn't matter.
"""

import test
from sys import exit

def permutes(s, path = ""):
    #paths = []
    if not s:
        yield path

    for i in range(0,len(s)):
        yield from permutes(s[:i] + s[i+1:], path + s[i])

def permutations(s):
    return list(set(permutes(s)))

def main():
    test.assert_equals(sorted(permutations('a')), ['a']);
    test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
    test.assert_equals(sorted(permutations('abc')), ['abc','acb','bac','bca','cab','cba'])
    test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

if __name__ == "__main__":
    main()
exit()

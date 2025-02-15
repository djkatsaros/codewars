"""
Kata Description:

Task:
Your task is to generate a palindrome string, using the specified length n, the specified characters c(all characters in c must be used at least once), and the code length should less than: python 55 characters javascript 62 characters
"""

palindrome=lambda n,s:s+s[-1]*(n-2*len(s)+1)+s[-2::-1]

soln = "palindrome=lambda n,s:s+s[-1]*(n-2*len(s)+1)+s[-2::-1]"



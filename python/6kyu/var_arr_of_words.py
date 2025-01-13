""" 
Kata Description:
Consider X as the aleatory variable that count the number of letters in a word. Write a function that, give in input an array of words (strings), calculate the variance of X. Max decimal of the variance : 4.

Some wiki: Variance , Aleatory variable

Example:

Consider "Hello" and "World":

X is { 5 } with P(X = 5) = 1 because the two words have the same length.
So E[X] = 5 x 1 = 5 and the standard formula for variance is E[(X - u)^2] so 1 x (5-5)^2 = 0 or you can calculate with the other formula E[X^2] - E[X]^2 = 5^2 x 1 - 5^2 = 0

Consider "Hi" and "World":

X is { 2, 5 } with P(X = 5) = 1/2 and P(X = 2) = 1/2.
So E[X] = 5 x 1/2 + 2 x 1/2 = 3.5 and the standard formula for variance is E[(X - u)^2] so 1/2 x (2-3.5)^2 + 1/2 x (5 - 3.5)^2 = 2.25 or you can calculate with the other formula E[X^2] - E[X]^2 = (5^2 x 1/2 + 2^2 x 1/2) - 3.5^2 = 2.25

"""

import test
from sys import exit

def variance(words):

    def get_probs(words):
        ''' returns a dictionary of probabilities for a word length'''
        lens=[len(s) for s in words]
        probs={}
        for l in lens:
            if l not in probs:
                probs[l] = 1/len(lens)
            else:
                probs[l] += 1/len(lens)
        return probs

    def get_expectation(probs):
        ''' takes a dictionary of numbers : probabilities X=num and returns expected value '''
        return sum([l*probs[l] for l in probs.keys()])

    pbs = get_probs(words)
    mu = get_expectation(pbs)
    return round(sum([pbs[l]*(l-mu)**2 for l in pbs.keys()]),4)

def main():
    # There weren't many sample tests in codewars...
    test.assert_equals(variance("Hello world".split()), 0)
    test.assert_equals(variance("Hi world".split()), 2.25)

if __name__ == "__main__":
    main()

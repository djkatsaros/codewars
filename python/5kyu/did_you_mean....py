"""
Kata Description:
I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.

You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.

Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed. E.g. the mistyped term berr is more similar to beer (1 letter to be replaced) than to barrel (3 letters to be changed in total).

Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.

Code Examples:

fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
fruits.find_most_similar('strawbery') # must return "strawberry"
fruits.find_most_similar('berry') # must return "cherry"

things = Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars'])
things.find_most_similar('coddwars') # must return "codewars"

languages = Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript'])
languages.find_most_similar('heaven') # must return "java"
languages.find_most_similar('javascript') # must return "javascript" (identical words are obviously the most similar)

I know, many of you would disagree that java is more similar to heaven than all the other ones, but in this kata it is ;)

Additional notes:

    there is always exactly one possible correct solution
"""

import test

def levenshtein_two_matrix_rows(str1, str2):
    """Recycled from 'bob's signs' kata"""
    # Get the lengths of the input strings
    m = len(str1)
    n = len(str2)

    # Initialize two rows for dynamic programming
    prev_row = [j for j in range(n + 1)]
    curr_row = [0] * (n + 1)

    # Dynamic programming to fill the matrix
    for i in range(1, m + 1):
        # Initialize the first element of the current row
        curr_row[0] = i

        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match, no operation needed
                curr_row[j] = prev_row[j - 1]
            else:
                # Choose the minimum cost operation
                curr_row[j] = 1 + min(
                    curr_row[j - 1],  # Insert
                    prev_row[j],      # Remove
                    prev_row[j - 1]    # Replace
                )

        # Update the previous row with the current row
        prev_row = curr_row.copy()

    # The final element in the last row contains the Levenshtein distance
    return curr_row[n]

class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        """ Use levenshtein dist to get the 'distances' between each wrd in words and term
        (i.e., number of changes we'd need to make). Answer is the word requiring the smallest number
        of changes."""
        dists = {}
        for wrd in self.words:
            dists[wrd] = levenshtein_two_matrix_rows(wrd, term)

        return min(dists, key=dists.get)

def main():
    words = ['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
    test_dict = Dictionary(words)
    test.assert_equals(test_dict.find_most_similar('strawbery'), 'strawberry')
    test.assert_equals(test_dict.find_most_similar('berry'), 'cherry')
    test.assert_equals(test_dict.find_most_similar('aple'), 'apple')

if __name__ == "__main__":
    main()

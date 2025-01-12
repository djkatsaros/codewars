from sys import exit
"""
KATA DESCRIPTION
A bookseller has lots of books classified in 26 categories labeled A, B, C, ..., Z. Each book has a code of at least 3 characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code is followed by a space and by a positive integer, which indicates the quantity of books of this code in stock.
Task

You will receive the bookseller's stocklist and a list of categories. Your task is to find the total number of books in the bookseller's stocklist, with the category codes in the list of categories. Note: the codes are in the same order in both lists.

Return the result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog).
Example

# the bookseller's stocklist:
"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"

# list of categories:
"A", "B", "C", "W"

# result:
"(A : 20) - (B : 114) - (C : 50) - (W : 0)"

Explanation:

    category A: 20 books (ABART)
    category B: 114 books = 25 (BKWRK) + 89 (BTSQZ)
    category C: 50 books (CDXEF)
    category W: 0 books
"""
import test

def stock_list(list_of_art, list_of_cat):
    out = {}
    for cat in list_of_cat:
        out[cat] = 0

    zero = True

    for art in list_of_art:
        split_ = art.split()
        for cat in list_of_cat:
            if split_[0][0] == cat:
                out[cat] += int(split_[1])
                if int(split_[1]) != zero:
                    zero = False

    out_str = ""
    for cat in list_of_cat:
        out_str += "(" + cat + " " + ":" + " " + str(out[cat]) +")" + " " + "-" + " "

    if zero:
        return ""
    else:
        return out_str[:-3]

def main():
    # example from description
    b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
    c = ["A", "B", "C", "W"]
    test.assert_equals(stock_list(b, c), "(A : 20) - (B : 114) - (C : 50) - (W : 0)")
    
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    test.assert_equals(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B"]
    test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")    

if __name__ == "__main__":
    main()

exit()

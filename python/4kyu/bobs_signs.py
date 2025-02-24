"""
Kata Description:
Overview

You need to help Bob be a good businessman and not charge people too much for his signs.
Description

Bob is running a business that creates signs for people. He can charge much less than his competitors because he charges by letter instead by the entire sign. He can take a sign and change a few letters to make a new sign much more cheaply than a competitor can make a sign from scratch.

The only problem is Bob is not very good at pricing these changes. He wants to be able to look at a sign and a customer's request and quickly be able to give the customer an estimate for the total cost.
Task

Define a function estimate(add_cost, remove_cost, old_sign, new_sign) -> minimum_cost that is adaptable to changes in the market, and can help Bob estimate prices quickly.

The first 2 arguments are the costs of doing an operation, of adding and removing a letter respectively.
The last 2 arguments are the old sign of the customer, and their request.

It should return the cost of changing the sign from the old message to the new message. If there are multiple ways to change the sign, it should return the cheapest way.
"""

import test

def estimate(add_cost, remove_cost, old, new):
    """DP approach. 
    Uses ideas related to the Levenshtein distance, which is really just 
    a semi-trivial/obvious distance metric between two strings.
    The real interesting part is the dp approach, mainly a memoiz application.
    memory optimize by only tracking two rows at a time"""
        
    m, n = len(old), len(new) 
    
    # initialize prev row
    prev_row =  [j * add_cost for j in range(n + 1)]
    DP_curr = [0] * (n + 1)
    
    for i in range(1, m + 1): 
        # initizlie DP_curr
        DP_curr[0] = i * remove_cost
        
        for j in range(1, n + 1):
            
            if old[i - 1] == new[j - 1]: # if the characters are the same, do nothing
                DP_curr[j] = prev_row[j -1]
                
            else:
                # minimum of removing or adding to make change
                DP_curr[j] = min(DP_curr[j-1] + add_cost, prev_row[j] + remove_cost)
        
        # make copy to actually make changes
        prev_row = DP_curr.copy()
    
    return DP_curr[n]

def main():
    test.assert_equals(estimate(5, 4, "totes", "toes"), 4)
    test.assert_equals(estimate(5, 4, "totes", "oats"), 13)


if __name__ == "__main__":
    main()

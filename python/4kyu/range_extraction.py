"""
Kata Description
 A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""

import test

def solution(l):
    """Basic idea:
    Iterate through the list of args 'l' 1 time. As we move through the list, construct and
    add string elements based on the formatting conditions to a list structure to later be joined.
    Formatting is based on if..
        (a) we have more than 2 consecutive elements that are also consecutive integers -> 'x-y' for x the min y the max
        (b) We have 2 consecutive elements that are also consecutive integers -> 'x,y'
        (c) We have an 'isolated' element -> 'x'.
        """

    out = []    # store all the formatted strings
    old = l[0]  # initialize a the 'old' element so we can track any consecutive streaks
    curr = old  # currently, our streak is 0
    ct = 0      # currently, our streak is 0
    for el in l[1:]:
        if old < el - 1: # if the streak has ended / hasn't begun, append to out based on the length of the streak
            if ct > 1:
                # formatting case (a)
                out += cand
                ct = 0
            elif ct == 1:
                # formatting case (b)
                out += [str(curr)] + [str(old)]
                ct = 0
            else:
                # formatting case (c)
                out += [str(old)]
            old = el
            curr = old
        else:
            # if we encounter another consecutive integer, add to ct to track streak.
            ct += 1
            cand = [str(curr) + '-' + str(el)] # update 'cand' formatted 'x-y' string
            old = el

    # repeat the logic of updating out but for the end.
    if ct > 1:
        out += cand
    elif ct == 1:
        out += [str(curr)] + [str(old)]
    else:
        out += [str(old)]

    # finally, return the joined out list.
    return ",".join(out)

def main():
    test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
    test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')    
    test.assert_equals(solution([-60, -59, -58, -55, -52, -50, -48, -45, -44, -42, -40, -37, -35, -32, -30, -27, -25, -23, -20, -17]), '-60--58,-55,-52,-50,-48,-45,-44,-42,-40,-37,-35,-32,-30,-27,-25,-23,-20,-17')
    test.assert_equals(solution([-57, -55, -52, -51, -50, -49, -46, -45, -43, -40, -39, -38, -37, -35, -32, -31, -28]), '-57,-55,-52--49,-46,-45,-43,-40--37,-35,-32,-31,-28')
    test.assert_equals(solution([-84, -83, -82, -81, -78, -75, -72, -70, -68, -65, -62, -59, -57, -54, -52, -49, -48, -45, -44, -41, -38]), '-84--81,-78,-75,-72,-70,-68,-65,-62,-59,-57,-54,-52,-49,-48,-45,-44,-41,-38')

if __name__ == "__main__":
    main()

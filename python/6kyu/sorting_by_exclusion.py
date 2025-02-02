"""
Task

Given an non-empty list or array (depending on language) of non-empty uppercase words, compute the minimum number of words, which, when removed from the list, leaves the rest of the list in strictly ascending lexicographic order.
Examples:

["THE","QUICK","BROWN","FOX","JUMPS","OVER","THE","LAZY","DOG"] should return 4, because removing "THE", "QUICK", "LAZY" & "DOG" leaves the sorted list ["BROWN","FOX","JUMPS","OVER","THE"].

["JACKDAW","LOVE","MY","BIG","SPHINX","OF","QUARTZ"] should return 2, because removing "BIG" & "SPHINX" leaves the sorted list ["JACKDAW","LOVE","MY","OF","QUARTZ"].

["A","A","A","A"] should return 3, because equal elements are NOT regarded as sorted, so all but one of them need to be removed.
"""

import test

def sort_by_exclusion(words):
    arr = words
    
    def sorted_idx(sub, val): # bisction/ binary search.
        l = 0 
        r = len(sub)-1
        while l <= r:
            mid = (l + r) // 2
            if sub[mid] >= val:
                r = mid - 1
            else:
                l = mid + 1
        return l
 
    sub = [arr[0]]
    for i in range(1, len(arr)):
        # use sorted_idx fcn to create a maximal sorted subarray. 
        if arr[i] > sub[-1]:
            sub.append(arr[i]) # append value to end of subarray if it is next in order
        else: 
            sub[sorted_idx(sub, arr[i])] = arr[i] # insert value at index maintaining the sortedness of subarray
                                                  # replaces whatever value was there -> maximal sorted.  
        print(sub, arr)
    return len(arr) - len(sub) 

def main():
    test.assert_equals(sort_by_exclusion(["M","O","A"]),1, "Remove A")
    test.assert_equals(sort_by_exclusion(["M","O","Q","A"]),1, "Remove A") 
                       
    test.assert_equals(sort_by_exclusion(["M","O","A","C"]),2, "Remove A, C (or M, O)")
    test.assert_equals(sort_by_exclusion(["M","A","O","C"]),2, "Remove A, C (or M, O)") 
    test.assert_equals(sort_by_exclusion(["M","O","Q","A","C"]),2, "Remove A, C") 

    test.assert_equals(sort_by_exclusion(["M","O","A","C","E"]),2, "Remove M, O") 
    test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E"]),3, "Remove A, C, E (or M, O, Q)") 

    test.assert_equals(sort_by_exclusion(["M","O","N","A","C","E"]),3, "Remove M, O, N")
    test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E","G"]),3, "Remove M, O, Q") 
    test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E","G","I","K","M"]),3, "Remove M, O, Q")

    test.assert_equals(sort_by_exclusion(["N","M","O","N","A","C","E"]),4, "Remove N, M, O, N") 
    test.assert_equals(sort_by_exclusion(["M","O","Q","A","C","E","G","I","L","K","M"]),4, "Remove M, O, Q, K") 
    
    test.assert_equals(sort_by_exclusion(["ANT","CAT","DOG","BEE","DOLPHIN","ZEBRA","LION","EAGLE"]),3,"Remove BEE, LION & EAGLE")
    test.assert_equals(sort_by_exclusion(["ANT","CAT","DOG","BEE","DOLPHIN","ZEBRA","EAGLE","LION"]),2,"Remove BEE & ZEBRA")
    test.assert_equals(sort_by_exclusion(["FOX","ANT","CAT","DOG","BEE","DOLPHIN","ZEBRA","EAGLE","LION","FOX"]),4,"Remove FOX, BEE, ZEBRA & FOX")

if __name__ == "__main__":
    main()

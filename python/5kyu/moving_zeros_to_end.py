"""
KATA DESCRIPTION

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]


"""
from sys import exit

def move_zeros(lst):
    zeros = 0
    out = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zeros += 1
        else:
            out.append(lst[i])

    print(out, zeros)
    for i in range(zeros):
        out.append(0)

    return out

def main():
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([0]) == [0]
    assert move_zeros([]) == [] 
   # print("Passed tests")

if __name__ == "__main__":
    main()
    print("Passed tests")


exit()

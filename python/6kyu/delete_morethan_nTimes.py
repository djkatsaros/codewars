"""
KATA DESCRIPTION
Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
He tells them that he will only sit for the session if they show the same motif at most N times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?
Task

Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].

"""
import test
from sys import exit

def delete_nth(order,max_e):
    out=[]
    for el in order:
        if out.count(el) < max_e:
            out.append(el)

    return out

def main():
    test.assert_equals(
            delete_nth([20, 37, 20, 21], 1),
            [20, 37, 21],
            "From list [20, 37, 20, 21], 1 you get",
        )
    test.assert_equals(
        delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
        [1, 1, 3, 3, 7, 2, 2, 2],
        "From list [1, 1, 3, 3, 7, 2, 2, 2, 2], 3 you get",
    )
    test.assert_equals(
        delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3),
        [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5],
        "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3 you get",
    )
    test.assert_equals(
        delete_nth([1, 1, 1, 1, 1], 5),
        [1, 1, 1, 1, 1],
        "From list [1, 1, 1, 1, 1], 5 you get",
    )
    test.assert_equals(delete_nth([], 5), [], "From list [], 5 you get")
    test.assert_equals(
        delete_nth([12, 39, 19, 39, 39, 19, 12], 1),
        [12, 39, 19],
        "From list [12, 39, 19, 39, 39, 19, 12], 1 you get",
    )


if __name__ == "__main__":
    main()
exit()

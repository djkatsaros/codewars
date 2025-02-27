"""
Kata Description
Task

Codewars expand their t-shirt selection so that there is one color corresponding to 1 or 2 levels:
White / 7,8kyu; Orange / 5,6kyu; Blue / 3,4kyu; Purple / 2kyu; Red / 1kyu; Black / 1dan.

At the beginning of each month Codewars receive a shipment of n t-shirts. There will always be an equal number of each color. Each user can only choose between 2 different colors when ordering a t-shirt. At the end of each month Codewars take all received orders and send t-shirts, but only if it is possible to grant all requests.

Given n and the list of orders placed, determine if Codewars have enough t-shirts to fulfill all orders (true) or must wait until the next month (false).
Input/Output

[input] integer n

The total number of t-shirts that Codewars have for the month. It is guaranteed that n is a multiple of 6.

6 ≤ n ≤ 36

[input] list of 2-tuples of colors orders

A list of tuples of colors representing the orders. Each order is a tuple of two colours (strings) - the color choices the user made. It is guaranteed that only the following colors are given: White, Orange, Blue, Purple, Red, Black.

0 ≤ len(orders) ≤ 20

[output] a boolean value

A boolean representing if all orders can be fulfilled for the month with the given t-shirts.
Example

For n = 6 and orders = [["Red", "Black"],["Red", "Black"]],

the output should be true.

Codewars have 6 shirts in stock, which means 1 of each color. If they send a red t-shirt for the first order, we can still send a black t-shirt for the second order. Thus, both orders can be fulfilled.

For n = 6 and orders = [["Red", "Black"], ["Red", "Black"], ["Red", "Black"]]

the output should be false.

Again, there is 1 t-shirt of each color. It is possible to fulfill the first two orders by sending 1 red and 1 black shirt, however there won't be any red/black shirts to fulfill the third order. Thus, it's impossible to fulfill all orders this month.
"""

import test

def make_stock(n):
    """takes in a multiple of 6, returns a stock hash table (dictionary)"""
    stock = {}
    colors = set(["White", "Orange", "Blue", "Purple", "Red", "Black"])
    depth = n // 6
    for color in colors:
        stock[color] = depth
    return stock

def codewars_tshirts(n, orders):
    stock = make_stock(n)

    def order(orders, stock):
        if not orders:
            return True

        ord = orders.pop()
        possible = False

        if stock[ord[0]] > 0:
            stock[ord[0]] -= 1
            possible = order(orders, stock)
            stock[ord[0]] += 1

        if stock[ord[1]] > 0:
            stock[ord[1]] -= 1
            possible = possible or order(orders, stock)
            stock[ord[1]] += 1

        orders.append(ord)

        return possible

    return order(orders, stock)

def main():
    test.assert_equals(codewars_tshirts(6,[("Red","Black"),("Red","Black")]),True)
    test.assert_equals(codewars_tshirts(6,[("Red","Black"),("Red","Black"),("Red","Black")]),False)
    test.assert_equals(codewars_tshirts(6,[("White","Purple"),("Purple","Blue"),("Blue","Orange"),("Orange","Red"),("Red","Black"),("Black","White")]),True)
    test.assert_equals(codewars_tshirts(24,[]),True)
    test.assert_equals(codewars_tshirts(6,[("Red","Black"),("Red","Black"),("Blue","Black")]),True)
    test.assert_equals(codewars_tshirts(6,[("Blue","Purple")]),True)
    test.assert_equals(codewars_tshirts(18,[("Black","Blue"),("Purple","Blue"),("Blue","White"),("White","Orange"),("White","Blue"),("Purple","White"),("White","Purple"),("White","Red"),("Blue","Purple"),("Orange","White"),("Black","Blue"),("Purple","Red"),("Blue","Red"),("Blue","White"),("Purple","White"),("Purple","Blue"),("Orange","Red")]),True)
    test.assert_equals(codewars_tshirts( 6, [ ("Purple","Black"), ("Black","Red"), ("Red","Purple"), ("Red","Purple"), ("White","Orange") ] ),False)

if __name__ == "__main__":
    main()


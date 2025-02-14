"""
Ridiculously wordy Kata Description:

    You are working as a salesperson, travelling around the world, visiting your customers. Every journey starts and ends in the office in London, and you are not allowed to come back to office until you visited all customers on the schedule you have got from your boss. Your boss will give you coordinates for each customer before you leave the office. You must claim travel expenses before you start journey, fixed cost £500 for any journey + £10 per each mile.

Your customers may be on a ship in middle of the ocean or in middle of desert or rainforest, in one of largest cities or smallest villages, in any country in the world, or anywhere on the Earth.

Because your boss has strange sense of humour, he sometimes gives you coordinates which does not exist on the Earth. You need to check all coordinate before you start to travel. If you miss this catch and start your journey, your boss will not pay any travel expenses, but worst, you will lose this kata. If you spot it before the travel, you can claim extra fully paid holiday day and you are winning this kata.

So, to summarise, there are two ways to win this kata - if your boss tries to catch you and you spot it, you are winning or if your boss gives you correct coordinates and you claim right expenses, you are winning. Otherwise, you are losing, but do not worry, you can try again.
Optimal Solution -> this kata

In Optimal Solution, you will have to visit exactly 4 customers. You will need to focus on optimal solution. With 4 customers, you have 24 options how to combine them, but your boss will only pay the shortest / the cheapest journey.
Nearest Neighbour Algorithm -> coming soon

In Nearest Neighbour Algorithm, you have to visit between 5 and 50 customers. You should be very familiar with validating data from your boss and calculating distance. Unfortunately, you will not be able to use the same approach as in Optimal Solution. Even your boss understands that you will not be able to plan the journey the most cost-effective way, because if you have maximum of 50 customers, you have 3.0414093 * 10^64 options to compare. Instead, your boss expects you to use Nearest Neighbour Algorithm. You can read more about it here: https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm.

Detailed instructions for Optimal Solution - THIS KATA

Now, you know the story and brief description of your task.

Your office is in London, England on with these coordinates:

OFFICE = {"lat": 51.49984, "long": -0.124663}

Your boss gives you with 4 customers to visit in the following format: Your boss gives you with 4 customers to visit in the following format:

[
  {"lat": 55.8642, "long": -4.2518},
  {"lat": 52.4862, "long": -1.8904},
  {"lat": 53.2268, "long": -0.5379},
  {"lat": 53.5229, "long": -1.1312}
]

Remember, all distances need to be in miles, you need to claim £10 per miles and fixed expense £500
To solve this kata successfully, please follow these steps:
1. Input Validation

Your first task is to check, if your boss gave you coordinates, or made a joke of you.
Any coordinates outside this range are invalid:
Valid latitude must be between -90 and 90
Valid longitude must be between -180 and 180

If input is valid, you have accurate information from your boss, so can proceed to next step. If the input is invalid return "I am claiming extra holiday!" since your boss is making joke at your expense.
2. You are expected to get optimal solution, best possible option what in this case means shortest distance

To calculate distance, use Haversine formula, with EARTH_RADIUS = 3959, due to working in miles.
Remember, you need to get best out of 24 possible travel options (because you have to visit 4 customers, you have 24 possible combinations to choose from). Do not forget that you need to travel from the office to first customer and back to the office from last customer.
3. Calculate your expenses

You are not expected to round decimal numbers at any point of this kata (rounding during calculation process may fail testing), and your boss is so good to you, that he accepts 0.01% tolerance between your calculation and his expectation.
Examples

Input 1 (invalid input - latitude is more than 90 and longitude is less than 180):

[
  {"lat": 90.8642, "long": -4.2518},
  {"lat": 52.4862, "long": -180.8904},
  {"lat": 53.2268, "long": -0.5379},
  {"lat": 53.5229, "long": -1.1312},
]

Output 1:

"I am claiming extra holiday!"

Input 2 (valid input):

[
  {"lat": 55.8642, "long": -4.2518},
  {"lat": 52.4862, "long": -1.8904},
  {"lat": 53.2268, "long": -0.5379},
  {"lat": 53.5229, "long": -1.1312}
]

Output 2:

7602

"""

import test
import numpy as np

INT_MAX = 9000000000000

EARTH_RADIUS = 3959
OFFICE = {"lat": 51.49984, "long": -0.124663} # office coordinates

from math import sin, cos, sqrt, atan2, radians

def Havers(lat1, lat2, lon1, lon2):

    R = EARTH_RADIUS

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

from itertools import permutations

def tsp(cost):
    """
    Computes TSP mincost using permutations.
    Brutally inefficient TBH"""
    # Number of nodes
    numNodes = len(cost)
    nodes = list(range(1, numNodes))

    minCost = float('inf')

    # Generate all permutations
    for perm in permutations(nodes):
        currCost = 0
        currNode = 0

        for node in perm:
            currCost += cost[currNode][node]
            currNode = node

        # Add the cost to return to the starting node
        currCost += cost[currNode][0]

        # Update the minimum cost
        minCost = min(minCost, currCost)

    return minCost

def travel_expenses(customers: list):
    # start your code here

    n = len(customers)

    for i in range(n):
        if abs(customers[i]["lat"]) <= 90.0 and abs(customers[i]["long"]) <= 180.0:
            pass
        else:
            return "I am claiming extra holiday!"


    # build cost matrix
    customers.insert(0, OFFICE)
    n = len(customers)
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cost[i][j] = 10 * Havers(customers[i]["lat"], customers[j]["lat"], customers[i]["long"], customers[j]["long"])
            #print(f"{cost[i][j]} is the distance from customer {customers[i]} to customer {customers[j]}")

    print(np.array(cost))
    cost = tsp(cost)

    return cost + 500

def main():
    test.assert_approx_equals(travel_expenses(
        [
            {"lat": 55.8642, "long": -4.2518},
            {"lat": 52.4862, "long": -1.8904},
            {"lat": 53.2268, "long": -0.5379},
            {"lat": 53.5229, "long": -1.1312},
        ]
    ), 7602, 0.1)    
    test.assert_equals(travel_expenses(
        [
            {"lat": 90.8642, "long": -4.2518},
            {"lat": 52.4862, "long": -180.8904},
            {"lat": 53.2268, "long": -0.5379},
            {"lat": 53.5229, "long": -1.1312},
        ]
    ),"I am claiming extra holiday!")

if __name__ == "__main__":
    main()

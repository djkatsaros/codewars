
"""
This kata is about the travelling salesman problem. You have to visit every city once and return to the starting point.

You get an adjacency matrix, which shows the distances between the cities. The total cost of path is defined as the sum of distances to travel from 1st city to the 2nd, from 2nd to 3rd, ..., and, finally, from last city to the 1st. Your task is to write a function, that returns a valid path with same or smaller cost, as compared to the reference solution.

Return a valid route as a list.

The "names" of the places are the indexes in the array, here is an example for a matrix:

     0 1 2

0    0 5 7
1    5 0 4
2    7 4 0

The starting point is always place 0. The routes are symmetric means the distance from 0 to 1 is always the same as from 1 to 0.

Example:

matrix = [
    [0,176,463],
    [176,0,125],
    [463,125,0]
]

# Possible outcomes
tsp(matrix) in [
    [0, 1, 2, 0],
    [0, 2, 1, 0]
]

Test Cases

There are:

    30 tests with 5 points
    30 tests with 20 points
    5 tests with 100 points

The total number of all possible routes can be calculated as:
(n−1)!2\frac{(n-1)!}{2}2(n−1)!​

A naive approach becomes transcomputational at 66 cities. So a bruteforce approach is not a way to go.
Note about results validation

If in the test your path has cost M, and reference path has cost N, then you get the score N/M for that test. You are not obliged to find optimal route in each test, but you have to get enough scores in a series of tests. For example, in a series with 30 tests you have to get 30 points.
"""


def dist_of_path(matrix, path):
    dist = 0
    for i, second in enumerate(path[1:]):
        first = path[i]
        dist += matrix[first][second]
    return dist

def greedy_tsp(matrix, start = 0):
    path = [start]
    distance = 0
    for _ in range(len(matrix)-1):
        string = matrix[path[-1]]
        dist = float('inf')
        for i, d in enumerate(string):
            if i in path:
                continue
            if d < dist:
                ind = i
                dist = d
        path.append(ind)
        distance += dist
    distance += matrix[path[-1]][0]
    path.append(start)
    return (path, distance)

def improved_nearest(matrix, path, distance):
    result = path
    for start in path[1:-1]:
        new_path, dist = greedy_tsp(matrix, start)
        new_path = new_path[:-1]
        ind = new_path.index(0)
        new_path = new_path[ind:] + new_path[:ind] + [0]
        dist = dist_of_path(matrix, new_path)
        if dist < distance:
            result = new_path
            distance = dist
    return (result, distance)

def tsp(matrix):
    path, dist = greedy_tsp(matrix)
    solution, distance = improved_nearest(matrix, path, dist)
    return solution



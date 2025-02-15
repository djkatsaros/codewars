"""
Kata Description:
    You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1]. Number of climb rounds between adjacent locations is defined as difference of location altitudes (ascending or descending).

Location altitude is defined as an integer number (0-9).
Path Finder Series:

    #1: can you reach the exit?
    #2: shortest path
    #3: the Alpinist
    #4: where are you?
    #5: there's someone here

"""

import test

from queue import PriorityQueue

def path_finder(area):
    topo = []
    for val in area.split('\n'):
        topo.append(list(map(int, val)))

    qu = PriorityQueue()
    memo = dict()
    m, n = len(topo), len(topo[0])

    start, finish = (0, 0), (m-1, n-1)

    neighbors = [(-1,0), (1,0), (0,1), (0,-1)]  # for each position, we need to check the cost of moving
                                                # to that position from each of these 4 points modulo bndries
    qu.put((0, start))                          # initiliaze the queue of points, and thereby the while loop

    while not qu.empty():
        curr_cost, curr_pos = qu.get()


        if curr_pos in memo and memo[curr_pos] <= curr_cost:
            # if we have already computed the cost to this position and got a lower cost, skip this pos,
            # go to next pos, cost pair in the queue
            continue

        memo[curr_pos] = curr_cost # otherwise, record cost to current position

        if curr_pos == finish: # stop when current position = end.
            break

        for pt in neighbors:
            # iterate through 4 neighbors, moving forward in the topo to new_pos.
            new_pos = (pt[0]+curr_pos[0], pt[1]+curr_pos[1])

            if 0 <= new_pos[0] < m and 0 <= new_pos[1] < n: # handles boundary cases.

                # compute the cost of moving to new_pos from curr_pos
                new_cost = abs(topo[new_pos[0]][new_pos[1]] - topo[curr_pos[0]][curr_pos[1]])

                if new_pos in memo and memo[new_pos] <= new_cost + curr_cost:
                    # if this new position is in memo already at a lower cost, don't append it, go to next pt in
                    # neighbors
                    continue

                qu.put((new_cost+curr_cost, new_pos))   # add the next cost/position to the queue if all the above
                                                        # passes

    return memo[finish]

def main():
    a = "\n".join([
      "000",
      "000",
      "000"
    ])

    b = "\n".join([
      "010",
      "010",
      "010"
    ])

    c = "\n".join([
      "010",
      "101",
      "010"
    ])

    d = "\n".join([
      "0707",
      "7070",
      "0707",
      "7070"
    ])

    e = "\n".join([
      "700000",
      "077770",
      "077770",
      "077770",
      "077770",
      "000007"
    ])

    f = "\n".join([
      "777000",
      "007000",
      "007000",
      "007000",
      "007000",
      "007777"
    ])

    g = "\n".join([
      "000000",
      "000000",
      "000000",
      "000010",
      "000109",
      "001010"
    ])
    h = '366\n345\n621'
    
    i = '031966954432\n847339916806\n352935896774\n496380581305\n620787904383\n219647585003\n764880381621\n759088684645\n301705000576\n643922886796\n238492016250\n584919086648'
    j = '11471452835212\n85097032636205\n15290360299147\n49718661542385\n62256602060344\n76663336913710\n38499887131575\n39855614147782\n66257522647815\n77545675382569\n67358380574853\n43313689358417\n72426606316303\n61288446995543'

    test.assert_equals(path_finder(a), 0)
    test.assert_equals(path_finder(b), 2)
    test.assert_equals(path_finder(c), 4)
    test.assert_equals(path_finder(d), 42)
    test.assert_equals(path_finder(e), 14)
    test.assert_equals(path_finder(f), 0)
    test.assert_equals(path_finder(g), 4)
    test.assert_equals(path_finder(h), 4)
    test.assert_equals(path_finder(i), 38)
    test.assert_equals(path_finder(j), 38)

if __name__ == "__main__":
    main()

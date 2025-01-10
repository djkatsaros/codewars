"""
KATA DESCRIPTION
Once upon a time, on a way through the old wild mountainous west,…

… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!
How I crossed a mountainous desert the smart way.

The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]

You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]

"""

from sys import exit
import test

#def assert_equals(a, b):
 #   assert a == b

def dir_reduc(arr):
    states = {'north' : 'south', 'south' : 'north' , 'east' : 'west', 'west' : 'east'}
    idx = 0
    while arr and idx < len(arr)-1:
        if states[arr[idx].lower()] == arr[idx+1].lower():
            arr.pop(idx)
            arr.pop(idx)
            if idx > 0:
                idx -= 1
        else:
            idx += 1

    print(idx, arr)

    return arr

def main():
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    test.assert_equals(dir_reduc(a), ['WEST'])
    a=["NORTH", "WEST", "SOUTH", "EAST"]
    test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] # ['WEST']
    test.assert_equals(dir_reduc(a), ['WEST'])
    a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"] # ['NORTH', 'NORTH']
    test.assert_equals(dir_reduc(a), ['NORTH', 'NORTH'])
    a = [] # []
    test.assert_equals(dir_reduc(a), []) 
    a=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] # []
    test.assert_equals(dir_reduc(a), [])
    a = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"] # ["NORTH"]
    test.assert_equals(dir_reduc(a), ["NORTH"])
    a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"] # ["EAST", "NORTH"]
    test.assert_equals(dir_reduc(a), ["EAST", "NORTH"])
    a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"] # ["NORTH", "EAST"])
    test.assert_equals(dir_reduc(a), ["NORTH", "EAST"])
    a = ["NORTH", "WEST", "SOUTH", "EAST"] # ["NORTH", "WEST", "SOUTH", "EAST"])
    test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
    a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
    test.assert_equals(dir_reduc(a), ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])  

if __name__ == "__main__":
    main()

exit()



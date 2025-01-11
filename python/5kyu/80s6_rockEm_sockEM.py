"""
KATA DESCRIPTION
You and your friends have been battling it out with your Rock 'Em, Sock 'Em robots, but things have gotten a little boring. You've each decided to add some amazing new features to your robot and automate them to battle to the death.

Each robot will be represented by an object. You will be given two robot objects, and an object of battle tactics and how much damage they produce. Each robot will have a name, hit points, speed, and then a list of battle tactics they are to perform in order. Whichever robot has the best speed, will attack first with one battle tactic.

Your job is to decide who wins.

Example:

 robot_1 = {
  "name": "Rocky",
  "health": 100,
  "speed": 20,
  "tactics": ["punch", "punch", "laser", "missile"]
 }
 robot_2 = {
   "name": "Missile Bob",
   "health": 100,
   "speed": 21,
   "tactics": ["missile", "missile", "missile", "missile"]
 }
 tactics = {
   "punch": 20,
   "laser": 30,
   "missile": 35
 }
 
 fight(robot_1, robot_2, tactics) -> "Missile Bob has won the fight."

robot2 uses the first tactic, "missile" because he has the most speed. This reduces robot1's health by 35. Now robot1 uses a punch, and so on.

Rules

    A robot with the most speed attacks first. If they are tied, the first robot passed in attacks first.
    Robots alternate turns attacking. Tactics are used in order.
    A fight is over when a robot has 0 or less health or both robots have run out of tactics.
    A robot who has no tactics left does no more damage, but the other robot may use the rest of his tactics.
    If both robots run out of tactics, whoever has the most health wins. If one robot has 0 health, the other wins. Return the message "{Name} has won the fight."
    If both robots run out of tactics and are tied for health, the fight is a draw. Return "The fight was a draw."

"""

import test
from sys import exit

def fight(robot_1, robot_2, tactics):
    l= max(len(robot_1["tactics"]), len(robot_2["tactics"]))
    print(robot_1, robot_2)

    if robot_1["speed"] >= robot_2["speed"]:
        for i in range(l):

            try:
                robot_2["health"] -= tactics[robot_1["tactics"][i]]
                if robot_2["health"] <= 0:
                    return robot_1["name"] + " has won the fight."
            except IndexError:
                pass

            try:
                robot_1["health"] -= tactics[robot_2["tactics"][i]]
                if robot_1["health"] <= 0:
                    return robot_2["name"] + " has won the fight."
            except IndexError:
                pass
#             print(robot_1["health"], robot_2["health"])
        if robot_1["health"] > robot_2["health"]:
            return robot_1["name"] + " has won the fight."

        elif robot_2["health"] > robot_1["health"]:
            return robot_2["name"] + " has won the fight."

        else:
            return "The fight was a draw."

    else:
        for i in range(l):

            try:
                robot_1["health"] -= tactics[robot_2["tactics"][i]]
                if robot_1["health"] <= 0:
                    return robot_2["name"] + " has won the fight."
            except IndexError:
                pass

            try:
                robot_2["health"] -= tactics[robot_1["tactics"][i]]
                if robot_2["health"] <= 0:
                    return robot_1["name"] + " has won the fight."
            except IndexError:
                pass

        if robot_2["health"] > robot_1["health"]:
            return robot_2["name"] + " has won the fight."

        elif robot_1["health"] > robot_2["health"]:
            return robot_1["name"] + " has won the fight."

        else:
            return "The fight was a draw."

def main():
    robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
    robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
    tactics = {"punch": 20, "laser": 30, "missile": 35}
    test.assert_equals(fight(robot_1, robot_2, tactics), "Missile Bob has won the fight.")

    robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
    robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
    tactics = {"punch": 20, "laser": 30, "missile": 35}
    test.assert_equals(fight(robot_1, robot_2, tactics), "Rocky has won the fight.")

if __name__ == "__main__":
    main()

exit()

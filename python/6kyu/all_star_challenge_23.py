"""
Kata Description
All Star Code Challenge #23

There is a certain multiplayer game where players are assessed at the end of the game for merit. Players are ranked according to an internal scoring system that players don't see.

You've discovered the formula for the scoring system!

Create a function called scoring() that takes an array of Player objects and returns an array of player names, in order of descending score (highest score is index 0, 2nd highest is index 1, etc.).

Each player's score is calculated as follows:

    Each normal kill is worth 100 points
    Each assist is worth 50 points
    Each point of damage done is worth 0.5 points
    Each point of healing done is worth 1 point
    The longest kill streak is worth 2^N, where N is the number of kills of the streak
    Environmental kills are worth 500 points (These are counted separately from normal kills)

For each of the above statistic, a Player object contains a respective "key:value" pairing. All values except the 'name' are integers.
"""

import test
from sys import exit

def compute_(player: dict):
    """Assumes a player dictionary structure of
    player =
        {
          "name": str,
          "norm_kill": int,
          "assist": int,
          "damage": int,
          "healing": int,
          "streak": int,
          "env_kill": int
                            } """
    return player['norm_kill']*100 + player['assist']*50 + player['damage']*0.5 + player['healing'] + 2**player['streak'] + player['env_kill']*500

def scoring(arr):
    scores = []
    for player in arr:
        scores.append((player['name'], compute_(player)))

    out = []
    for (name, score) in sorted(scores, key = lambda tup: -tup[1]):
        out.append(name)

    return out

def main():
    p1 = {
          "name": "JuanPablo",
          "norm_kill": 5,
          "assist": 12,
          "damage": 3200,
          "healing": 0,
          "streak": 4,
          "env_kill": 1
        }
    p2 = {
      "name": "ProfX",
      "norm_kill": 2,
      "assist": 14,
      "damage": 600,
      "healing": 1500,
      "streak": 0,
      "env_kill": 0
    }
    p3 = {
      "name": "Ajna",
      "norm_kill": 1,
      "assist": 8,
      "damage": 900,
      "healing": 30,
      "streak": 3,
      "env_kill": 5
    }
    test.assert_equals(scoring([p1]),["JuanPablo"])
    test.assert_equals(scoring([p1, p2]),["JuanPablo","ProfX"])
    test.assert_equals(scoring([]),[])
    test.assert_equals(scoring([p3, p1, p2]),["Ajna", "JuanPablo","ProfX"])
    test.assert_equals(scoring([p1, p3, p2]),["Ajna", "JuanPablo","ProfX"])

if __name__ == "__main__":
    main()

exit()

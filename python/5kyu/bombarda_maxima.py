"""
Kata Description:
You have a bomb, which you can throw in a field. Bomb explodes in this way:

- - - - -      - - - - -
- - - - -      - - * - -
- - ⇩ - -  =>  - * * * -
- - - - -      - - * - -   # bomb is thrown in the center of the field
- - - - -      - - - - -   # bomb explosion traverses 1 cell up, down, right left

Bomb explosion always starts in the cell bomb was thrown into.

there might be other bombs in the field (symbol B on the graphic). If bomb is within the explosion radius it will also explode.

- - - - -        - - * - -
- - B - -        - * * * -
- - ⇩ - -   =>   - * * * -
- - - - -        - - * - -
- - - - -        - - - - -  # other bombs might exist in the field!
                            # if we now throw bomb in the center of the field, 
                            # initial explosion will cause a chain explosion

It is not forbidden to throw a bomb in a cell with already existing bomb.

You will be given a field as an Array of Arrays of strings, where symbol - represents an empty cell, and symbol B represents an existing bomb.

Cell, that have experienced an explosion at least once is treated as damaged.

Your task is to find maximum posible amount of damaged cells when you throw the bomb in a field. Retun integer.
    """

import test

def explode(coord):
    coords = [(coord[0], coord[1]), (coord[0] - 1, coord[1]),
              (coord[0], coord[1] - 1), (coord[0] + 1, coord[1]),
              (coord[0], coord[1] + 1)]
    return coords

def spread(coord, field):
    triggered = set()
    bombs = [coord]
    while bombs:
        c = bombs.pop()
        for pt1, pt2 in explode((c[0], c[1])):
            if (pt1 < 0) or (pt1 >= len(field)) or (pt2< 0) or (pt2 >= len(field[0])):
                continue
            fire = (pt1, pt2)
            if fire not in triggered:
                triggered.add(fire)
                if field[fire[0]][fire[1]] == 'B':
                    bombs.append(fire)

    return len(triggered)

def bombarda(field):
    damages = []
    for idx, row in enumerate(field):
        for jdx in range(len(row)):
            damages += [spread((idx, jdx), field)]

    return max(damages)

# from test suite
def format_field(field):
    """Helper method to join the 2D field array into a single string, \n delimited."""
    return "\n".join(" ".join(row) for row in field)

def main():
    field = [
        "- - - - -".split(" "),
        "- - - - -".split(" "),
        "- - - - -".split(" "),
        "- - - - -".split(" "),
        "- - - - -".split(" "),
    ]
    formatted_field = format_field(field)
    test.assert_equals(bombarda(field), 5, f"For input:\n{formatted_field}")
    field = [
        "- - - - -".split(" "),
        "- - - - -".split(" "),
        "- B - - -".split(" "),
        "- - B - -".split(" "),
        "- - - - -".split(" "),
    ]
    formatted_field = format_field(field)
    test.assert_equals(bombarda(field), 10, f"For input:\n{formatted_field}")
    field = [
        "- - - - -".split(" "),
        "- - B - -".split(" "),
        "- B - B -".split(" "),
        "- - B - -".split(" "),
        "- - - - -".split(" "),
    ]
    formatted_field = format_field(field)
    test.assert_equals(bombarda(field), 13, f"For input:\n{formatted_field}")

if __name__ == "__main__":
    main()

def rgb(round: str) -> tuple[int, int, int]:
    cubes = map(lambda r: r.strip(), round.split(','))
    r = 0
    g = 0
    b = 0
    for c in cubes:
        amt, col = c.split()
        if col == "red":
            r = int(amt)
        elif col == "blue":
            b = int(amt)
        elif col == "green":
            g = int(amt)
    return r, g, b

if __name__ == "__main__":
    lines = open("2/cube_conundrum.txt").read().splitlines()
    gamesum = 0
    powersum = 0
    for l in lines:
        gameno, cubes = l.split(':', 1)
        gameno = int(gameno[5:])
        rounds = map(lambda c: c.strip(), cubes.split(';'))
        maxred = 0
        maxgreen = 0
        maxblue = 0
        for round in rounds:
            r, g, b = rgb(round)
            maxred = max(maxred, r)
            maxgreen = max(maxgreen, g)
            maxblue = max(maxblue, b)
        if maxred <= 12 and maxgreen <= 13 and maxblue <= 14:
            gamesum += gameno
        powersum += maxred * maxgreen * maxblue
    # part 1 answer
    print(gamesum)
    # part 2 answer
    print(powersum)

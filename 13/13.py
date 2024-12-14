import re


class Game:
    def __init__(self, ax, ay, bx, by, tx, ty):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.tx = tx
        self.ty = ty


def parse_chunk(chunk):
    ax, ay = map(int, re.findall("\+(\d+)", chunk[0]))
    bx, by = map(int, re.findall("\+(\d+)", chunk[1]))
    tx, ty = map(int, re.findall("=(\d+)", chunk[2]))
    return Game(ax, ay, bx, by, tx, ty)


def solve_game(game):
    max_a = min(game.tx // game.ax, game.ty // game.ay)
    max_b = min(game.tx // game.bx, game.ty // game.by)

    solutions = []
    for a in range(max_a + 1):
        for b in range(max_b + 1):
            if (
                a * game.ax + b * game.bx == game.tx
                and a * game.ay + b * game.by == game.ty
            ):
                solutions.append((a, b))

    return (
        min(map(lambda s: s[0] * 3 + s[1] * 1, solutions)) if len(solutions) > 0 else 0
    )


def count_a():
    return sum(map(solve_game, get_games()))


def get_games():
    games = []
    chunk = []
    for line in open("./13.data").readlines():
        if len(line) == 1:
            games.append(parse_chunk(chunk))
            chunk = []
        else:
            chunk.append(line)
    games.append(parse_chunk(chunk))
    return games


print("a:", count_a())

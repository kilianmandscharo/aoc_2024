def is_in_bounds(grid, point):
    return (
        point[0] >= 0
        and point[0] < len(grid[0])
        and point[1] >= 0
        and point[1] < len(grid)
    )


def add_points(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub_points(a, b):
    return (a[0] - b[0], a[1] - b[1])


def get_antinodes_a(grid, a, b):
    antinodes = []
    first = add_points(a, sub_points(a, b))
    second = add_points(b, sub_points(b, a))
    if is_in_bounds(grid, first):
        antinodes.append(first)
    if is_in_bounds(grid, second):
        antinodes.append(second)
    return antinodes


def get_antinodes_b(grid, a, b):
    antinodes = [a, b]
    dir_first = sub_points(a, b)
    dir_second = sub_points(b, a)
    while True:
        a = add_points(a, dir_first)
        if not is_in_bounds(grid, a):
            break
        antinodes.append(a)
    while True:
        b = add_points(b, dir_second)
        if not is_in_bounds(grid, b):
            break
        antinodes.append(b)
    return antinodes


def make_point_map(grid):
    point_map = dict()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c = grid[y][x]
            if not c.isalnum():
                continue
            if c in point_map:
                point_map[c].append((x, y))
            else:
                point_map[c] = [(x, y)]
    return point_map

def count(grid, antinode_func):
    point_map = make_point_map(grid)
    antinodes = []
    for key in point_map:
        for a in point_map[key]:
            for b in point_map[key]:
                if a == b:
                    continue
                new_antinodes = antinode_func(grid, a, b)
                antinodes += new_antinodes
    return len(set(antinodes))

grid = list(map(lambda l: [c for c in l.strip()], open("./08.data").readlines()))


print("a:", count(grid, get_antinodes_a))
print("b:", count(grid, get_antinodes_b))

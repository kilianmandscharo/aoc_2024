def count_a(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "X":
                continue
            for d in [
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
            ]:
                s = ""
                pos = (x, y)
                for _ in range(3):
                    pos = (pos[0] + d[0], pos[1] + d[1])
                    if (
                        pos[0] < 0
                        or pos[0] == len(grid[0])
                        or pos[1] < 0
                        or pos[1] == len(grid)
                    ):
                        break
                    s += grid[pos[1]][pos[0]]
                if s == "MAS":
                    total += 1
    return total


def count_b(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (
                y == 0
                or x == 0
                or y == len(grid) - 1
                or x == len(grid[0]) - 1
                or grid[y][x] != "A"
            ):
                continue
            top_left = grid[y - 1][x - 1]
            top_right = grid[y - 1][x + 1]
            bottom_left = grid[y + 1][x - 1]
            bottom_right = grid[y + 1][x + 1]
            if (
                (top_left == "M" and bottom_right == "S")
                or (top_left == "S" and bottom_right == "M")
            ) and (
                (top_right == "S" and bottom_left == "M")
                or (top_right == "M" and bottom_left == "S")
            ):
                total += 1
    return total


grid = list(map(lambda l: [c for c in l.strip()], open("./04.data").readlines()))

print("a:", count_a(grid))
print("b:", count_b(grid))

def count_edges(patch, grid, target):
    min_x = min_y = float("inf")
    max_x = max_y = 0
    for p in patch:
        min_x = min(min_x, p[0])
        max_x = max(max_x, p[0])
        min_y = min(min_y, p[1])
        max_y = max(max_y, p[1])
    edges = 0
    for y in range(max_y - min_y + 1):
        curr = "X"
        for x in range(max_x - min_x + 1):
            val = grid[y][x]
            prev_curr = grid[y - 1][x - 1] if y - 1 > min_y and x - 1 > min_x else None
            prev_val = grid[y - 1][x] if y - 1 > min_y else None
            if curr != val and (y == 0 or (x == 0 and grid[y - 1][x] != val)):
                print("beginning", x, y)
                edges += 1
            elif curr != val and x > 0 and (prev_curr != curr or prev_val != val):
                print("middle", x, y)
                edges += 1
            elif val == target and x == max_x and prev_val != val:
                edges += 1
                print("end", x, y)
            curr = val
    print("=====")
    for x in range(max_x - min_x + 1):
        curr = "X"
        for y in range(max_y - min_y + 1):
            val = grid[y][x]
            prev_curr = grid[y - 1][x - 1] if y - 1 > min_y and x - 1 > min_x else None
            prev_val = grid[y][x - 1] if x - 1 > min_y else None
            print(curr, val)
            if curr != val and (x == 0 or (y == 0 and grid[y][x - 1] != val)):
                print("beginning", x, y)
                edges += 1
            elif curr != val and y > 0 and (prev_curr != curr or prev_val != val):
                print("middle", x, y)
                edges += 1
            elif (
                val == target
                and y == max_y
                and prev_val != val
                and (x == 0 or grid[y][x - 1] != val)
            ):
                edges += 1
                print("end", x, y)
            curr = val
            print("---")
    print(edges)


grid = [
    ["E", "E", "E", "E"],
    ["E", "X", "X", "X"],
    ["E", "E", "E", "E"],
    ["E", "X", "X", "X"],
    ["E", "E", "E", "E"],
]

patch = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (3, 2),
    (0, 3),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4),
]

count_edges(patch, grid, "E")

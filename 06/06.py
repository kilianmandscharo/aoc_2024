def is_oob(grid, position):
    return (
        position[0] < 0
        or position[0] == len(grid[0])
        or position[1] < 0
        or position[1] == len(grid)
    )


def is_obstacle(grid, position):
    return grid[position[1]][position[0]] == "#"


def take_step(grid, position, direction, visited):
    new_position = (position[0] + direction[0], position[1] + direction[1])
    if is_oob(grid, new_position):
        return None, direction
    if is_obstacle(grid, new_position):
        return position, (direction[1] * -1, direction[0])
    visited.append(new_position)
    return new_position, direction


def get_starting_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                return (x, y)


def count_a(grid):
    position = get_starting_position(grid)
    direction = (0, -1)
    visited = [position]
    while position != None:
        position, direction = take_step(grid, position, direction, visited)
    return len(set(visited))


def take_step_b(grid, position, direction, obstacles_hit, obstacles_hit_count):
    new_position = (position[0] + direction[0], position[1] + direction[1])
    if is_oob(grid, new_position):
        return None, direction
    if is_obstacle(grid, new_position):
        pos_and_dir = (position[0], position[1], direction[0], direction[1])
        obstacles_hit.append(pos_and_dir)
        if pos_and_dir in obstacles_hit_count:
            obstacles_hit_count[pos_and_dir] += 1
        else:
            obstacles_hit_count[pos_and_dir] = 1
        return position, (direction[1] * -1, direction[0])
    return new_position, direction


def check_if_loop(grid):
    position = get_starting_position(grid)
    direction = (0, -1)
    obstacles_hit = []
    obstacles_hit_count = dict()
    while True:
        if position == None:
            return False
        for i in range(len(obstacles_hit) - 4):
            if (
                obstacles_hit_count[obstacles_hit[i]] > 1
                and obstacles_hit_count[obstacles_hit[i + 1]] > 1
                and obstacles_hit_count[obstacles_hit[i + 2]] > 1
                and obstacles_hit_count[obstacles_hit[i + 3]] > 1
            ):
                return True
        position, direction = take_step_b(
            grid, position, direction, obstacles_hit, obstacles_hit_count
        )


def count_b(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(x, y)
            if grid[y][x] == "^" or grid[y][x] == "#":
                continue
            grid[y][x] = "#"
            if check_if_loop(grid):
                total += 1
            grid[y][x] = "."
    return total


grid = list(map(lambda l: [c for c in l.strip()], open("./06.data").readlines()))

print("a:", count_a(grid))
print("b:", count_b(grid))

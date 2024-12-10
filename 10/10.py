class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def pos(self):
        return (self.x, self.y)


def get_neighbors(grid, node):
    neighbors = []
    if node.x > 0:
        neighbors.append(Node(node.x - 1, node.y, grid[node.y][node.x - 1]))
    if node.x < len(grid[0]) - 1:
        neighbors.append(Node(node.x + 1, node.y, grid[node.y][node.x + 1]))
    if node.y > 0:
        neighbors.append(Node(node.x, node.y - 1, grid[node.y - 1][node.x]))
    if node.y < len(grid) - 1:
        neighbors.append(Node(node.x, node.y + 1, grid[node.y + 1][node.x]))
    return [n for n in neighbors if n.val - 1 == node.val]


def get_trailhead_score_a(grid, x, y):
    found = dict()
    unvisited = [Node(x, y, 0)]
    while len(unvisited) > 0:
        node = unvisited.pop()
        if node.val == 9:
            found[node.pos()] = True
            continue
        unvisited += get_neighbors(grid, node)
    return len(found)


def count_a(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 0:
                continue
            total += get_trailhead_score_a(grid, x, y)
    return total


def get_trailhead_score_b(grid, x, y):
    count = 1
    unvisited = [Node(x, y, 0)]
    while len(unvisited) > 0:
        node = unvisited.pop()
        if node.val == 9:
            continue
        neighbors = get_neighbors(grid, node)
        unvisited += neighbors
        count += len(neighbors) - 1
    return count


def count_b(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 0:
                continue
            total += get_trailhead_score_b(grid, x, y)
    return total


grid = list(map(lambda l: [int(c) for c in l.strip()], open("./10.data")))

print("a:", count_a(grid))
print("b:", count_b(grid))

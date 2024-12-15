def get_neighbors(grid, x, y, val):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(grid[0]) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(grid) - 1:
        neighbors.append((x, y + 1))
    return [n for n in neighbors if grid[n[1]][n[0]] == val]


def count_a(grid):
    total = 0
    visited = dict()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in visited:
                continue
            unvisited = [(x, y)]
            patch = []
            area = 0
            perimeter = 0
            while len(unvisited) > 0:
                px, py = unvisited.pop(0)
                patch.append((px, py))
                visited[(px, py)] = True
                neighbors = get_neighbors(grid, px, py, grid[py][px])
                area += 1
                perimeter += 4 - len(neighbors)
                for n in neighbors:
                    if (n[0], n[1]) not in visited and (n[0], n[1]) not in unvisited:
                        unvisited.append(n)
            total += area * perimeter
    return total


# def get_dirs():
#     return [
#         (1, 0),
#         (0, 1),
#         (-1, 0),
#         (0, -1),
#     ]
#
#
# def get_outline(x, y, neighbors):
#     outline = []
#     for d in get_dirs():
#         pos = (x + d[0], y + d[1])
#         if pos not in neighbors:
#             outline.append(pos)
#     return outline
#
#
# def is_neighbor(ax, ay, bx, by):
#     for dx, dy in get_dirs():
#         if ax + dx == bx and ay + dy == by:
#             return True
#     return False
#
#
# def get_unvisited(outlines, visited):
#     for p in outlines:
#         if p not in visited:
#             return p
#     return None
#
#
# def find_neighbor_index(x, y, outlines):
#     for i in range(len(outlines)):
#         if is_neighbor(x, y, outlines[i][0], outlines[i][1]):
#             return i
#     return None
#
#
# def count_edges(outlines):
#     edges = 1
#     ax, ay = outlines.pop(0)
#     while len(outlines) > 0:
#         print(ax, ay)
#         idx = find_neighbor_index(ax, ay, outlines)
#         if idx == None:
#             print("not found")
#             edges += 1
#             ax, ay = outlines.pop(0)
#         else:
#             ax, ay = outlines.pop(idx)
#     return edges
#
#
# def count_b(grid):
#     total = 0
#     visited = dict()
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if (x, y) in visited:
#                 continue
#             unvisited = [(x, y)]
#             outlines = []
#             area = 0
#             while len(unvisited) > 0:
#                 px, py = unvisited.pop(0)
#                 visited[(px, py)] = True
#                 neighbors = get_neighbors(grid, px, py, grid[py][px])
#                 if len(neighbors) < 4:
#                     outlines += get_outline(px, py, neighbors)
#                 area += 1
#                 for n in neighbors:
#                     if (n[0], n[1]) not in visited and (n[0], n[1]) not in unvisited:
#                         unvisited.append(n)
#             edges = count_edges(outlines)
#             print(area, edges)
#             total += area * edges
#     return total


grid = list(map(lambda l: [c for c in l.strip()], open("./12.test.data").readlines()))

print("a:", count_a(grid))
# print("b:", count_b(grid))

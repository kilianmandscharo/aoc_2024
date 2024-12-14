from copy import deepcopy


class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self, w, h):
        self.px = (self.px + self.vx) % w
        self.py = (self.py + self.vy) % h


def parse_line(l):
    a, b = l.split(" ")
    px, py = map(int, a.replace("p=", "").split(","))
    vx, vy = map(int, b.replace("v=", "").split(","))
    return px, py, vx, vy


def count_quadrants(robots, w, h):
    x = w // 2
    y = h // 2
    counts = [0, 0, 0, 0]
    for r in robots:
        if r.px < x:
            if r.py < y:
                counts[0] += 1
            elif r.py > y:
                counts[3] += 1
        elif r.px > x:
            if r.py < y:
                counts[1] += 1
            elif r.py > y:
                counts[2] += 1
    return counts[0] * counts[1] * counts[2] * counts[3]


def count_a(robots, w, h):
    for _ in range(100):
        for robot in robots:
            robot.move(w, h)
    return count_quadrants(robots, w, h)


def count_b(robots, w, h):
    i = 0
    while True:
        for robot in robots:
            robot.move(w, h)
        i += 1
        avg_d = avg_distance(robots)
        if avg_d < 50:
            print(i, avg_d)
            print_robots(robots, w, h)
            break
    return i


def avg_distance(robots):
    total = 0
    count = 0
    for r in robots:
        r_total = 0
        r_count = 0
        for other in robots:
            if r == other:
                continue
            r_total += abs(r.px - other.px) + abs(r.py - other.py)
            r_count += 1
        total += r_total / r_count
        count += 1
    return total / count


def print_robots(robots, w, h):
    grid = [["." for _ in range(w)] for _ in range(h)]
    for r in robots:
        val = grid[r.py][r.px]
        if isinstance(val, int):
            grid[r.py][r.px] += 1
        else:
            grid[r.py][r.px] = 1
    for l in grid:
        print("".join(map(str, l)))


robots = list(map(lambda l: Robot(*parse_line(l)), open("./14.data").readlines()))

print("a:", count_a(deepcopy(robots), 101, 103))
print("b:", count_b(deepcopy(robots), 101, 103))

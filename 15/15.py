dirs = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


class Entity:
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.prev_x = None
        self.prev_y = None

    def pos(self):
        return (self.x, self.y)

    def move(self, d):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = self.x + d[0]
        self.y = self.y + d[1]

    def rewind(self):
        if self.prev_x != None:
            self.x = self.prev_x
        if self.prev_y != None:
            self.y = self.prev_y

    def __str__(self):
        return f"{self.x}, {self.y} -> {self.kind}"


class Grid:
    def __init__(self, lines):
        self.entities = []
        self.robot = None
        self.width = len(lines[0])
        self.height = len(lines)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == ".":
                    continue
                entity = Entity(x, y, c)
                self.entities.append(entity)
                if entity.kind == "@":
                    self.robot = entity

    def add(self, p, d):
        return (p[0] + d[0], p[1] + d[1])

    def get(self, p):
        for e in self.entities:
            if p == e.pos():
                return e
        return None

    def move_robot(self, d):
        entities = [self.robot]
        new_pos = self.add(self.robot.pos(), d)
        while True:
            entity = self.get(new_pos)
            if entity == None:
                for e in entities:
                    e.move(d)
                break
            elif entity.kind == "O":
                entities.append(self.get(new_pos))
            else:
                break
            new_pos = self.add(new_pos, d)

    def print(self):
        grid = [["." for _ in range(self.width)] for _ in range(self.height)]
        for e in self.entities:
            grid[e.y][e.x] = e.kind
        for line in grid:
            print("".join(line))

    def get_count(self):
        return sum(
            map(lambda e: 100 * e.y + e.x if e.kind == "O" else 0, self.entities)
        )


def count_a():
    lines = list(map(lambda l: l.strip(), open("./15.data").readlines()))
    split_index = lines.index("")
    instructions = "".join(lines[split_index + 1 :])
    grid = Grid(lines[:split_index])
    for c in instructions:
        grid.move_robot(dirs[c])
    return grid.get_count()


print("a:", count_a())

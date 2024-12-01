from functools import reduce

x, y = map(
    lambda l: sorted(map(int, l)),
    zip(*map(lambda x: x.strip().split(), open("./a.data").readlines())),
)

print(
    "a:",
    reduce(
        lambda acc, item: acc + (abs(item[0] - item[1])),
        zip(x, y),
        0,
    ),
)

print("b:", reduce(lambda acc, item: acc + item * y.count(item), x, 0))

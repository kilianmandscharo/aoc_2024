from re import findall
from functools import reduce
import operator

print(
    "a:",
    reduce(
        lambda acc, match: acc + int(match[0]) * int(match[1]),
        findall(r"mul\((\d{1,3}),(\d{1,3})\)", open("./03.data").read()),
        0,
    ),
)

print(
    "b:",
    reduce(
        lambda acc, match: (
            (
                acc[0] + reduce(operator.mul, map(int, match[4:-1].split(",")), 1)
                if "mul" in match and acc[1]
                else acc[0]
            ),
            False if "don't" in match else True if "do" in match else acc[1],
        ),
        findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", open("./03.data").read()),
        (0, True),
    )[0],
)

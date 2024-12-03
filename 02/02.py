from functools import reduce


def countValid(validationFunc):
    return reduce(
        lambda acc, l: acc + 1 if validationFunc(l) else acc,
        map(
            lambda l: list(map(int, l.strip().split())),
            open("./02.data").readlines(),
        ),
        0,
    )


def isValidA(row):
    if row[0] == row[1]:
        return False
    for i in range(0, len(row) - 1):
        diff = row[i + 1] - row[i] if row[0] - row[1] < 0 else row[i] - row[i + 1]
        if diff < 1 or diff > 3:
            return False
    return True


def isValidB(row):
    if isValidA(row):
        return True
    for i in range(len(row)):
        if isValidA(row[:i] + row[i + 1 :]):
            return True
    return False


print("a:", countValid(isValidA))
print("b:", countValid(isValidB))

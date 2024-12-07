def make_permutations(operators, n, current, collected):
    if len(current) == n:
        collected.append(current)
        return collected
    for operator in operators:
        make_permutations(operators, n, current.copy() + [operator], collected)
    return collected


def evaluate(left, right, operator):
    if operator == "+":
        return left + right
    elif operator == "*":
        return left * right
    elif operator == "||":
        return int(str(left) + str(right))
    raise Exception("invalid operator")


def process_line(line, operators):
    line = line.split(": ")
    result = int(line[0])
    values = list(map(int, line[1].split(" ")))
    for operator_list in make_permutations(operators, len(values) - 1, [], []):
        total = values[0]
        i = 1
        while i < len(values):
            total = evaluate(total, values[i], operator_list[i - 1])
            i += 1
        if total == result:
            return total
    return 0


data = list(map(lambda l: l.strip(), open("./07.data").readlines()))

print("a:", sum(map(lambda l: process_line(l, ["+", "*"]), data)))
print("b:", sum(map(lambda l: process_line(l, ["+", "*", "||"]), data)))

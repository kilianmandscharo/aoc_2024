from functools import reduce


def is_rule_satisfied(update, i, rule):
    try:
        return i < update.index(rule)
    except:
        return True


def is_update_valid(update, rule_map):
    for i, val in enumerate(update):
        if not val in rule_map:
            continue
        for rule in rule_map[val]:
            if not is_rule_satisfied(update, i, rule):
                return False
    return True


def get_rule_map(rules):
    rule_map = dict()
    for rule in rules:
        a, b = rule.split("|")
        if a in rule_map:
            rule_map[a].append(b)
        else:
            rule_map[a] = [b]
    return rule_map


def count_a(rule_map, updates):
    return reduce(
        lambda acc, update: (
            acc
            if not is_update_valid(update, rule_map)
            else acc + int(update[len(update) // 2])
        ),
        updates,
        0,
    )


def get_smallest_invalid(update, i, rules):
    smallest = None
    for rule in rules:
        if not is_rule_satisfied(update, i, rule):
            rule_idx = update.index(rule)
            smallest = rule_idx if smallest == None else min(smallest, rule_idx)
    return smallest


def fix_update(update, rule_map):
    for i in range(len(update)):
        while True:
            if update[i] not in rule_map:
                break
            rules = rule_map[update[i]]
            smallest = get_smallest_invalid(update, i, rules)
            if smallest == None:
                break
            update[i], update[smallest] = update[smallest], update[i]


def count_b(rule_map, updates):
    total = 0
    for update in updates:
        if is_update_valid(update, rule_map):
            continue
        fix_update(update, rule_map)
        total += int(update[len(update) // 2])
    return total


data = list(map(lambda l: l.strip(), open("./05.data").readlines()))
idx = data.index("")
rules, updates = data[:idx], data[idx + 1 :]
rule_map = get_rule_map(rules)
updates = list(map(lambda u: u.split(","), updates))

print("a:", count_a(rule_map, updates))
print("b:", count_b(rule_map, updates))

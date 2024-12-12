def count(n):
    stones = {
        0: 1,
        4: 1,
        4979: 1,
        24: 1,
        4356119: 1,
        914: 1,
        85734: 1,
        698829: 1,
    }

    def insert_val(d, k, v):
        if k in d:
            d[k] += v
        else:
            d[k] = v

    for _ in range(n):
        new = dict()
        for stone in stones:
            count = stones[stone]
            if count == 0:
                continue
            if stone == 0:
                insert_val(new, 1, count)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                right = int(s[: len(s) // 2])
                left = int(s[len(s) // 2 :])
                insert_val(new, left, count)
                insert_val(new, right, count)
            else:
                val = stone * 2024
                insert_val(new, val, count)
        stones = new

    return sum(stones.values())


print("a:", count(25))
print("b:", count(75))

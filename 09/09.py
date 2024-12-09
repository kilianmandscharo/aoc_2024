def make_blocks(line):
    blocks = []
    id = 0
    is_file = True
    for c in line:
        if is_file:
            blocks += int(c) * [id]
            id += 1
        else:
            blocks += int(c) * ["."]
        is_file = not is_file
    return blocks


def blocks_checksum(blocks):
    total = 0
    for i, b in enumerate(blocks):
        if b == ".":
            continue
        total += i * int(b)
    return total


def count_a(line):
    blocks = make_blocks(line)
    empty_idx = 0
    block_idx = len(blocks) - 1
    while True:
        while empty_idx <= block_idx and blocks[empty_idx] != ".":
            empty_idx += 1
        while block_idx >= empty_idx and blocks[block_idx] == ".":
            block_idx -= 1
        if empty_idx >= block_idx:
            break
        blocks[empty_idx], blocks[block_idx] = blocks[block_idx], blocks[empty_idx]
    return blocks_checksum(blocks)


def find_free_empty_space(blocks, idx):
    start = idx
    while start < len(blocks) and blocks[start] != ".":
        start += 1
    end = start
    while end < len(blocks) and blocks[end] == ".":
        end += 1
    return start, end


def find_file(blocks, id):
    end = len(blocks) - 1
    while end > 0 and blocks[end] != id:
        end -= 1
    start = end
    while start > 0 and blocks[start - 1] == id:
        start -= 1
    return start, end + 1


def count_b(line):
    blocks = make_blocks(line)
    start_empty = end_empty = 0
    start_file = end_file = len(blocks)
    id = blocks[-1]
    while id >= 0:
        start_file, end_file = find_file(blocks, id)
        start_empty, end_empty = find_free_empty_space(blocks, 0)
        id -= 1
        while end_empty - start_empty < end_file - start_file:
            start_empty, end_empty = find_free_empty_space(blocks, end_empty)
        if start_empty >= end_file:
            continue
        for i in range(end_file - start_file):
            blocks[start_empty + i], blocks[start_file + i] = (
                blocks[start_file + i],
                blocks[start_empty + i],
            )
    return blocks_checksum(blocks)


line = open("./09.data").read().strip()

print("a:", count_a(line))
print("b:", count_b(line))

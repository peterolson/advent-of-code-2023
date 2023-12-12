with open("input/12.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

records = []
for line in lines:
    [springs, groups] = line.split()
    groups = [int(group) for group in groups.split(",")]
    records.append((springs, groups))


def get_arrangements(springs, groups):
    if len(groups) == 0:
        if "#" in springs:
            return 0
        return 1
    broken = springs.count("#")
    remaining_sum = sum(groups)
    if broken > remaining_sum:
        return 0
    unknown = springs.count("?")
    if broken + unknown < remaining_sum:
        return 0

    next_group = groups[0]
    groups_tail = groups[1:]
    min_tail_length = sum(groups_tail) + len(groups_tail)
    region_to_fill = springs[:-min_tail_length] if len(groups_tail) > 0 else springs
    original_region_to_fill = region_to_fill
    while (
        min_tail_length > 0
        and springs[-min_tail_length] == "#"
        and region_to_fill[-1] == "#"
    ):
        region_to_fill += "#"
        min_tail_length -= 1

    i = 0
    total_count = 0
    while i + next_group <= len(original_region_to_fill):
        chunk = region_to_fill[i : i + next_group]
        if "." in chunk:
            i += 1
            continue
        if i + next_group < len(springs) and springs[i + next_group] == "#":
            i += 1
            continue
        if "#" in region_to_fill[0:i]:
            break
        total_count += get_arrangements(springs[i + next_group + 1 :], groups_tail)
        if chunk[0] == "#":
            break
        i += 1
    return total_count


def get_arrangements_split(springs, groups):
    if len(springs) < 6 or len(groups) < 2:
        count = get_arrangements(springs, groups)
        return count
    middle = len(groups) // 2
    middle_group = groups[middle]
    left_groups = groups[:middle]
    right_groups = groups[middle + 1 :]
    start = sum(left_groups) + len(left_groups)
    end = len(springs) - sum(right_groups) - len(right_groups)

    i = start
    total_count = 0
    while i + middle_group <= end:
        slice = springs[i : i + middle_group]
        if "." in slice:
            i += 1
            continue
        if i > 0 and springs[i - 1] == "#":
            i += 1
            continue
        if i + middle_group < len(springs) and springs[i + middle_group] == "#":
            i += 1
            continue
        left_count = get_arrangements_split(springs[: i - 1], left_groups)
        if left_count == 0:
            i += 1
            continue
        right_count = get_arrangements_split(
            springs[i + middle_group + 1 :], right_groups
        )
        total_count += left_count * right_count
        i += 1
    return total_count


counts = [get_arrangements_split(springs, groups) for springs, groups in records]
print(sum(counts))

records = [(((springs + "?") * 5)[:-1], groups * 5) for springs, groups in records]
total = 0
for i, record in enumerate(records):
    count = get_arrangements_split(*record)
    print(i, count)
    total += count
print(total)

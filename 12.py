from itertools import combinations

with open("input/12.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

records = []
for line in lines:
    [springs, groups] = line.split()
    groups = [int(group) for group in groups.split(",")]
    records.append((springs, groups))


def get_arrangements(springs, groups, depth=0):
    prefix = "    " * depth
    # print(prefix, springs, groups)
    if len(groups) == 0:
        if "#" in springs:
            return 0
        # print(prefix + "yay!")
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
        # print(prefix, region_to_fill, chunk, i)
        if "." in chunk:
            i += 1
            continue
        if i + next_group < len(springs) and springs[i + next_group] == "#":
            i += 1
            continue
        if "#" in region_to_fill[0:i]:
            break
        total_count += get_arrangements(
            springs[i + next_group + 1 :], groups_tail, depth + 1
        )
        if chunk[0] == "#":
            break
        i += 1
    return total_count


def get_arrangements_2(record):
    springs, groups = record
    total_damaged = sum(groups)
    unknown = springs.count("?")
    known_damaged = springs.count("#")
    missing_damaged = total_damaged - known_damaged
    arrangements = combinations(range(unknown), missing_damaged)
    valid_arrangements = 0
    for combination in arrangements:
        # replace ? with combination
        arrangement = ""
        i = 0
        for spring in springs:
            if spring == "?":
                if i in combination:
                    arrangement += "#"
                else:
                    arrangement += "."
                i += 1
            else:
                arrangement += spring
        arrangement_groups = [
            len(group) for group in arrangement.replace(".", " ").strip().split()
        ]
        if arrangement_groups == groups:
            valid_arrangements += 1
    return valid_arrangements


total_1 = 0
total_2 = 0
for record in records:
    count_1 = get_arrangements(*record)
    count_2 = get_arrangements_2(record)
    if count_1 != count_2:
        print(record, count_1, count_2)
    total_1 += count_1
    total_2 += count_2
print(total_1, total_2)

# arrangement_counts = []
# for i, record in enumerate(records):
#     springs, groups = record
#     counts = get_arrangements(springs, groups, 0, 0)
#     arrangement_counts.append(counts)

# print(sum(arrangement_counts))

# arrangement_counts = []
# for i, record in enumerate(records):
#     springs, groups = record
#     counts = get_arrangements(springs, groups, 0, 0)
#     double_counts = get_arrangements(springs + "?" + springs, groups * 2, 0, 0)
#     ratio = double_counts / counts
#     total = counts * ratio ** 4
#     triple_counts = get_arrangements(springs + "?" + springs + "?" + springs, groups * 3, 0, 0)
#     ratio_2 = triple_counts / counts
#     total_2 = counts * ratio_2 ** 2
#     print(i, counts, double_counts, triple_counts, ratio, ratio_2, total, total_2)

#     # 0 23570904
# print(sum(arrangement_counts))

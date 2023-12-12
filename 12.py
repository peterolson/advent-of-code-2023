with open("input/12.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

records = []
for line in lines:
    [springs, groups] = line.split()
    groups = [int(group) for group in groups.split(",")]
    records.append((springs, groups))

def get_arrangements(springs, groups, spring_start, group_start):
    if len(groups) - group_start == 0:
        if springs[spring_start:].count("#") > 0:
            return (0, 0)
        reaches_end = spring_start > len(springs)
        return (1, 1 if reaches_end else 0)
    next_group = groups[group_start]
    total_count = 0
    total_reaches_end = 0
    i = spring_start
    while i + next_group <= len(springs):
        s = springs[i]
        if s == ".":
            i += 1
            continue
        if s == "#" or s == "?":
            slice = springs[i:i+next_group]
            slice_is_valid = slice.count(".") == 0
            after_is_valid = i+next_group == len(springs) or springs[i+next_group] != "#"
            if slice_is_valid and after_is_valid:
                (count, reaches_end) = get_arrangements(springs, groups, i + next_group + 1, group_start + 1)
                total_count += count
                total_reaches_end += reaches_end

            if s == "#":
                    break
        i += 1

    return (total_count, total_reaches_end)
            


arrangement_counts = []
for i, record in enumerate(records):
    springs, groups = record
    counts, reaches_end = get_arrangements(springs, groups, 0, 0)
    arrangement_counts.append(counts)

print(sum(arrangement_counts))

arrangement_counts = []
for i, record in enumerate(records[:1]):
    springs, groups = record
    counts, reaches_end = get_arrangements(springs, groups, 0, 0)
    not_reaches_end = counts - reaches_end
    counts_prefix, reaches_end_prefix = get_arrangements("?" + springs, groups, 0, 0)
    not_reaches_end_prefix = counts_prefix - reaches_end_prefix
    counts_postfix, reaches_end_postfix = get_arrangements(springs + "?", groups, 0, 0)
    not_reaches_end_postfix = counts_postfix - reaches_end_postfix
    counts_shifted, reaches_end_shifted = get_arrangements(springs, groups, 1, 0)
    not_reaches_end_shifted = counts_shifted - reaches_end_shifted
        
    # 0 23570904
print(sum(arrangement_counts))
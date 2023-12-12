with open("input/12.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

records = []
for line in lines:
    [springs, groups] = line.split()
    groups = [int(group) for group in groups.split(",")]
    records.append((springs, groups))

def get_chunk_arrangements(chunk : str, groups : list[int], group_start : int, dict : dict[int, int]):
    if len(chunk) == 0:
        print("end", group_start)
        dict[group_start] = dict.get(group_start, 0) + 1
        return
    next_group = groups[0]
    i = 0
    while i + next_group <= len(chunk):
        is_valid = i + next_group == len(chunk) or chunk[i + next_group] == "?"
        print(chunk, i, next_group, is_valid)
        if is_valid:
            get_chunk_arrangements(chunk[i + next_group + 1:], groups, group_start + 1, dict)
        i += 1
    dict[group_start] = dict.get(group_start, 0) + 1
            
def get_arrangements(record):
    springs, groups = record
    chunks = [chunk for chunk in springs.split(".") if len(chunk) > 0]
    queue = [(chunks[0], 0, {}, 1)]
    grand_total = 0
    while len(queue) > 0:
        print(queue)
        chunk, i, dict, total = queue.pop(0)
        get_chunk_arrangements(chunk, groups, i, dict)
        print(dict)
        for group_start, count in dict.items():
            if group_start == len(groups) and i == len(chunks) - 1:
                grand_total += total * count
            elif i < len(chunks) - 1:
                queue.append((chunks[i + 1], group_start, {}, total * count))

get_arrangements(records[0])

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
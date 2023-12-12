from itertools import combinations

with open("input/12.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

records = []
for line in lines:
    [springs, groups] = line.split()
    groups = [int(group) for group in groups.split(",")]
    records.append((springs, groups))

def get_arrangements(record):
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
        arrangement_groups = [len(group) for group in arrangement.replace(".", " ").strip().split()]
        if arrangement_groups == groups:
            valid_arrangements += 1
    return valid_arrangements


arrangement_counts = []
for i, record in enumerate(records):
    counts = get_arrangements(record)
    arrangement_counts.append(counts)
    print(i, counts)
print(sum(arrangement_counts))

for i, record in enumerate(records):
    springs, groups = record
    records[i] = springs * 5, groups * 5

arrangement_counts = []
for i, record in enumerate(records):
    counts = get_arrangements(record)
    arrangement_counts.append(counts)
    print(i, counts)
print(sum(arrangement_counts))
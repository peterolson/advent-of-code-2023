with open("input/5.txt", "r") as f:
    lines = f.readlines()

seeds = lines[0].split(": ")[1].strip().split()
seeds = [int(x) for x in seeds]

source = None
destination = None

mappings = dict()

for i in range(1, len(lines)):
    line = lines[i].strip()
    if line.endswith(":"):
        map_name = line.split(" ")[0]
        (source, _to, destination) = map_name.split("-")
        mappings[source] = (destination, [])
    if len(line.split()) == 3:
        (destination_range, source_range, range_length) = [int(x) for x in line.split()]
        mappings[source][1].append((destination_range, source_range, range_length))


def get_destination(source, mapping):
    (destination, ranges) = mapping
    for destination_range, source_range, range_length in ranges:
        if source >= source_range and source < source_range + int(range_length):
            return (destination, destination_range + (source - source_range))
    return (destination, source)


def get_location(seed):
    key = "seed"
    while key != "location":
        (key, seed) = get_destination(seed, mappings[key])
    return seed


locations = [get_location(seed) for seed in seeds]

print(f"Part 1: {min(locations)}")


def get_destination_ranges(start, length, ranges):
    ranges = sorted(ranges, key=lambda x: x[1])
    overlapping_ranges = [
        range
        for range in ranges
        if range[1] <= start <= range[1] + range[2]
        or range[1] <= start + length <= range[1] + range[2]
        or start <= range[1] <= start + length
        or start <= range[1] + range[2] <= start + length
    ]
    bound_ranges = []
    for range in overlapping_ranges:
        if range[1] < start:
            bound_ranges.append(
                (
                    range[0] + (start - range[1]),
                    range[1] + (start - range[1]),
                    min(length, range[2] - (start - range[1])),
                )
            )
        elif range[1] + range[2] > start + length:
            bound_ranges.append(
                (range[0], range[1], range[2] - (range[1] + range[2] - start - length))
            )
        else:
            bound_ranges.append(range)
    filled_ranges = []
    s = start
    for range in bound_ranges:
        if range[1] > s:
            filled_ranges.append((s, s, range[1] - s))
        s = range[1] + range[2]
        filled_ranges.append(range)
    if s < start + length:
        filled_ranges.append((s, s, start + length - s))
    return [(range[0], range[2]) for range in filled_ranges]


def ranges_to_ranges(source_ranges, destination):
    ranges = mappings[destination][1]
    destination_ranges = []
    for start, length in source_ranges:
        destination_ranges.extend(get_destination_ranges(start, length, ranges))
    return destination_ranges


def traverse_ranges(start, length):
    destination = "seed"
    destination_ranges = [(start, length)]
    while destination != "location":
        destination_ranges = ranges_to_ranges(destination_ranges, destination)
        destination = mappings[destination][0]
    return destination_ranges


seed_pairs = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]

all_ranges = []
for seed_pair in seed_pairs:
    all_ranges.extend(traverse_ranges(seed_pair[0], seed_pair[1]))

lowest = min([range[0] for range in all_ranges])

print(f"Part 2: {lowest}")

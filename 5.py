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
    for (destination_range, source_range, range_length) in ranges:
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

def get_ranges(start, length, ranges):
    destination_ranges = []
    mapped_ranges = []
    for (destination_range, source_range, range_length) in ranges:
        if source_range <= start < source_range + range_length:
            destination_start = destination_range + (start - source_range)
            destination_range_length = min(length, range_length - (start - source_range))
            destination_ranges.append((destination_start, destination_range_length))
            mapped_ranges.append((start, destination_range_length))
        elif source_range <= start + length < source_range + range_length:
            destination_start = destination_range
            destination_range_length = start + length - source_range
            destination_ranges.append((destination_start, destination_range_length))
            mapped_ranges.append((source_range, destination_range_length))
    mapped_ranges = sorted(mapped_ranges, key=lambda x: x[0])
    unmapped_ranges = []
    if len(mapped_ranges) == 0:
        unmapped_ranges = [(start, length)]
    else:
        s = start
        for (m_start, m_length) in mapped_ranges:
            if s < m_start:
                unmapped_ranges.append((s, m_start - s))
            s = m_start + m_length
        if s < start + length:
            unmapped_ranges.append((s, start + length - s))
    return destination_ranges + unmapped_ranges

def traverse_ranges(start, length):
    key = "seed"
    destination_ranges = [(start, length)]
    while key != "location":
        (key, ranges) = mappings[key]
        new_destination_ranges = []
        for (destination_start, destination_length) in destination_ranges:
            new_destination_ranges += get_ranges(destination_start, destination_length, ranges)
        destination_ranges = new_destination_ranges
        print(key, destination_ranges)
        if sum([x[1] for x in destination_ranges]) != length:
            print(key, destination_ranges, length)
            print("MISMATCH")
    return sorted(new_destination_ranges, key=lambda x: x[0])

seed_pairs = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
ranges = [traverse_ranges(seed_pair[0], seed_pair[1])[0] for seed_pair in seed_pairs]
ranges = sorted(ranges, key=lambda x: x[0])
print(f"Part 2: {ranges[0][0]}")
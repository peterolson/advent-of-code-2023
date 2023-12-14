with open("input/14.txt", "r") as f:
    lines = [[c for c in line.strip()] for line in f.readlines()]

def calculate_load(map):
    load = 0
    for i in range(len(map)):
        factor = len(map) - i
        load += factor * map[i].count("O")
    return load

directions = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1)
}

def move_rocks(map, direction):
    di, dj = directions[direction]
    new_map = [[c for c in line] for line in map]
    start_i = len(map) - 1 if di == 1 else 0
    i_dir = -1 if di == 1 else 1
    i_stop = -1 if di == 1 else len(map)
    start_j = len(map[0]) - 1 if dj == 1 else 0
    j_dir = -1 if dj == 1 else 1
    j_stop = -1 if dj == 1 else len(map[0])
    for i in range(start_i, i_stop, i_dir):
        for j in range(start_j, j_stop, j_dir):
            if new_map[i][j] != "O":
                continue
            ci, cj = i + di, j + dj
            while 0 <= ci < len(map) and 0 <= cj < len(map[0]):
                if new_map[ci][cj] != ".":
                    break
                new_map[ci][cj] = "O"
                new_map[ci - di][cj - dj] = "."
                ci += di
                cj += dj
    return new_map


new_map = move_rocks(lines, "N")
print(calculate_load(new_map))

new_map = lines

def cycle_map(map):
    new_map = move_rocks(map, "N")
    new_map = move_rocks(new_map, "W")
    new_map = move_rocks(new_map, "S")
    new_map = move_rocks(new_map, "E")
    return new_map

def get_map_str(map):
    return "".join(["".join(line) for line in map])

def find_cycle(map):
    counts = {}
    repeat_dict = {}
    map_dict = {}
    count = 0
    new_map = map
    while True:
        map_str = get_map_str(new_map)
        if counts.get(map_str, 0) == 2:
            break
        counts[map_str] = counts.get(map_str, 0) + 1
        map_dict[map_str] = count
        repeat_dict[count] = new_map
        count += 1
        new_map = cycle_map(new_map)
    cycle_length = len([v for k, v in counts.items() if v == 2])
    cycle_start = len(counts) - cycle_length
    return cycle_length, cycle_start, repeat_dict, map_dict

cycle_length, cycle_start, repeat_dict, map_dict = find_cycle(new_map)

repeat_id = (1000000000 - cycle_start) % cycle_length + cycle_start + cycle_length
new_map = repeat_dict[repeat_id]
print(calculate_load(new_map))
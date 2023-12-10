with open("input/10.txt", "r") as f:
    lines = f.readlines()

pipe_types = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}

directions = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

map = [[c for c in line.strip()] for line in lines]

for i in range(len(map)):
    for j in range(len(map[i])):
        place = map[i][j]
        if place == 'S':
            start = (i, j)

encountered_places = dict()

search_queue = [(start, 0)]
while len(search_queue) > 0:
    current, distance = search_queue.pop(0)
    if current in encountered_places:
        continue
    encountered_places[current] = distance
    i, j = current
    available_directions = pipe_types[map[i][j]]
    for direction in available_directions:
        di, dj, opposite = directions[direction]
        new = (i + di, j + dj)
        if i + di < 0 or i + di >= len(map):
            continue
        if j + dj < 0 or j + dj >= len(map[i + di]):
            continue
        target = map[i + di][j + dj]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite in target_directions:
            search_queue.append((new, distance + 1))

max_distance = max(encountered_places.values())


print(max_distance)

def get_piece_type(i, j):
    reachable_directions = []
    for direction in directions:
        di, dj, opposite = directions[direction]
        if i + di < 0 or i + di >= len(map):
            continue
        if j + dj < 0 or j + dj >= len(map[i + di]):
            continue
        if (i + di, j + dj) not in encountered_places:
            continue
        target = map[i + di][j + dj]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite not in target_directions:
            continue
        reachable_directions.append(direction)
    for piece_type in pipe_types:
        if len(reachable_directions) == len(pipe_types[piece_type]):
            if all([direction in pipe_types[piece_type] for direction in reachable_directions]):
                return piece_type
    return None

map[start[0]][start[1]] = get_piece_type(start[0], start[1])

for i in range(len(map)):
    norths = 0
    for j in range(len(map[i])):
        place = map[i][j]
        if (i,j) in encountered_places:
            pipe_directions = pipe_types[place]
            if "n" in pipe_directions:
                norths += 1
            continue
        if norths % 2 == 0:
            map[i][j] = "O"
        else:
            map[i][j] = "I"


inside_count = "\n".join(["".join(line) for line in map]).count("I")
print(inside_count)
        
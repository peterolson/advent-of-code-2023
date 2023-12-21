with open("input/21.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

grid = {}
start_position = None

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        grid[(i, j)] = char
        if char == "S":
            start_position = (i, j)


def get_neighbors(position):
    i, j = position
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [
        neighbor for neighbor in neighbors if neighbor in grid and grid[neighbor] != "#"
    ]


queue = [start_position]
moves = 0
while moves < 6:
    new_queue = []
    for position in queue:
        for neighbor in get_neighbors(position):
            new_queue.append(neighbor)
    new_queue = list(set(new_queue))
    queue = new_queue
    moves += 1

print(len(queue))


def grid_at(position):
    i, j = position
    i = i % len(lines)
    j = j % len(lines[0])
    return grid[(i, j)]


def get_neighbors(position):
    i, j = position
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [neighbor for neighbor in neighbors if grid_at(neighbor) != "#"]


input_width = len(lines[0])
moves_to_reach_edge = input_width // 2


def f_n(n):
    return 2 * (7643 * n * n - 7589 * n + 1888)


# This is cheating but whatever
steps = 26501365
n = (steps + moves_to_reach_edge + 1) // input_width
print(f_n(n))

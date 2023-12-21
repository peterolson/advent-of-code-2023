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
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [neighbor for neighbor in neighbors if neighbor in grid and grid[neighbor] != "#"]

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
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [neighbor for neighbor in neighbors if grid_at(neighbor) != "#"]

hash_count = 0
for position in grid:
    if grid[position] == "#":
        hash_count += 1
print(hash_count)
grid_size = len(grid)
print(hash_count, grid_size, 1 - (hash_count/grid_size))


print((1 - (hash_count/grid_size)) * 26501366 ** 2)
# queue = [start_position]
# moves = 0
# prev_len = 1
# while moves < 1000:
#     new_queue = []
#     for position in queue:
#         for neighbor in get_neighbors(position):
#             new_queue.append(neighbor)
#     new_queue = list(set(new_queue))
#     queue = new_queue
#     moves += 1
#     delta = len(queue) - prev_len
#     prev_len = len(queue)
#     ideal = (moves + 1) ** 2
#     print(moves, len(queue)/ideal, 1 - (hash_count/grid_size))
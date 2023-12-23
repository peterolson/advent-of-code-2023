with open("input/23.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
hiking_map = dict()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        hiking_map[(i, j)] = char
        
starting_pos = (0,lines[0].index("."))
ending_pos = (len(lines) - 1, lines[-1].index("."))

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

max_path_length = 0

def find_longest_path(starting_pos, ending_pos, hiking_map, directions, visited, length_so_far):
    global max_path_length
    queue = [(starting_pos, length_so_far)]

    while len(queue) > 0:
        pos, length = queue.pop(0)
        visited.add(pos)
        if pos == ending_pos:
            if length > max_path_length:
                max_path_length = length
                print("Longest path so far: " + str(max_path_length))
            return length
        allowable_directions = directions.values()
        if hiking_map[pos] in directions:
            allowable_directions = [directions[hiking_map[pos]]]
        options = []
        for direction in allowable_directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos not in visited and new_pos in hiking_map and hiking_map[new_pos] != "#":
                options.append(new_pos)
        if len(options) == 1:
            queue.append((options[0], length + 1))
        elif len(options) > 1:
            longest_paths = []
            for option in options:
                new_visited = visited.copy()
                longest_paths.append(find_longest_path(option, ending_pos, hiking_map, directions, new_visited, length + 1))
            return max(longest_paths)
    return 0

longest_path = find_longest_path(starting_pos, ending_pos, hiking_map, directions, set(), 0)
print(longest_path)

def display_path(path):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if (i, j) in path:
                print("O", end="")
            else:
                print(char, end="")
        print()
        

# replace all slopes with .

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char in directions:
            hiking_map[(i, j)] = "."
            
longest_path = find_longest_path(starting_pos, ending_pos, hiking_map, directions, set(), 0)
            
print(longest_path)
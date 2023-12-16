with open("input/16.txt", "r") as f:
    lines = [[c for c in line.strip()] for line in f.readlines()]
    

mirrors = {
    "/": (0,-1),
    "\\": (0,1),
}    

start = (0,0)
direction = (0,1)




def find_energized(queue):
    energized = set()
    encountered = set()
    while len(queue) > 0:
        pos, direction = queue.pop(0)
        (i,j) = pos
        if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]):
            continue
        if (pos, direction) in encountered:
            continue
        encountered.add((pos, direction))
        
        energized.add(pos)
        c = lines[i][j]
        if c == "|" and direction[0] == 0:
            queue.append(((i+1, j), (1,0)))
            queue.append(((i-1, j), (-1,0)))
            continue
        elif c == "-" and direction[1] == 0:
            queue.append(((i, j+1), (0,1)))
            queue.append(((i, j-1), (0,-1)))
            continue
        if c == "/":
            direction = (-direction[1], -direction[0])
        elif c == "\\":
            direction = (direction[1], direction[0])
        queue.append(((i+direction[0], j+direction[1]), direction))
    return len(energized)
   
        
print(find_energized([(start, direction)]))
    
top_row = [((0, j), (1,0)) for j in range(len(lines[0]))]
bottom_row = [((len(lines)-1, j), (-1,0)) for j in range(len(lines[0]))]
left_col = [((i, 0), (0,1)) for i in range(len(lines))]
right_col = [((i, len(lines[0])-1), (0,-1)) for i in range(len(lines))]

all_paths = top_row + bottom_row + left_col + right_col
energized_paths = [find_energized([path]) for path in all_paths]
print(max(energized_paths))
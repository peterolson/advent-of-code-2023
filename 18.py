with open("input/18.txt", "r") as f:
    lines = [line for line in f.readlines()]
    
directions = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}
    
def parse_instruction(line):
    direction, distance, color = line.strip().split()
    d = directions[direction]
    dist = int(distance)
    color = color[2:-1]
    return d, dist, color

instructions = [parse_instruction(line) for line in lines]

vertex = (0, 0)
vertices = [vertex]
for d, dist, color in instructions:
    new_vertex = (vertex[0] + d[0] * dist, vertex[1] + d[1] * dist)
    vertices.append(new_vertex)
    vertex = new_vertex
    
ys = sorted(set([v[1] for v in vertices]), reverse=True)
prev_xs = []
prev_length = 0
area = 0
for i, y in enumerate(ys[:-1]):
    xs = [v[0] for v in vertices if v[1] == y]
    carry_over = [x for x in prev_xs if x not in xs]
    new = [x for x in xs if x not in prev_xs]
    xs = sorted(set(carry_over + new))
    x_pairs = list(zip(xs, xs[1:]))
    length = sum([x2 - x1 + 1 for x1, x2 in x_pairs])
    height = abs(y - ys[i+1])
    print(xs, length, height)
    if i > 0:
        area += abs(length - prev_length)
        print(abs(length - prev_length))
    area += length * height
    print(area)
    if i == len(ys) - 2:
        area += length
    print(area)
    prev_xs = xs
    prev_length = length
    
print(area)
with open("input/18.txt", "r") as f:
    lines = [line for line in f.readlines()]

directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

direction_pairs = {
    "UR": "F",
    "UL": "7",
    "DR": "L",
    "DL": "J",
    "RU": "J",
    "RD": "7",
    "LU": "L",
    "LD": "F",
}

starting_positions = {
    ("F", "R"): (-0.5, 0.5),
    ("F", "D"): (0.5, -0.5),
    ("7", "D"): (0.5, 0.5),
    ("7", "L"): (-0.5, -0.5),
    ("L", "R"): (0.5, 0.5),
    ("L", "U"): (-0.5, -0.5),
    ("J", "L"): (0.5, -0.5),
    ("J", "U"): (-0.5, 0.5),
}


def parse_instruction(line):
    direction, distance, color = line.strip().split()
    color = color[2:-1]
    return direction, int(distance), color


instructions = [parse_instruction(line) for line in lines]


def area(p):
    return 0.5 * abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in segments(p)))


def segments(p):
    return zip(p, p[1:] + [p[0]])


def get_area(instructions):
    vertex = (0, 0)
    vertices = []
    for i, instruction in enumerate(instructions):
        direction = instruction[0]
        dist = instruction[1]
        d = directions[direction]
        next_instruction = instructions[(i + 1) % len(instructions)]
        next_direction = next_instruction[0]
        corner_type = direction_pairs[direction + next_direction]
        vertex = (
            vertex[0] + d[0] * dist,
            vertex[1] + d[1] * dist,
            corner_type,
            next_direction,
        )
        vertices.append(vertex)

    new_vertices = []
    for i, (x1, y1, corner_type, next_direction) in enumerate(vertices):
        dx, dy = starting_positions[(corner_type, next_direction)]
        x = x1 + dx
        y = y1 + dy
        new_vertices.append((x, y))

    return int(area(new_vertices))


print(get_area(instructions))

new_instructions = []
for instruction in instructions:
    direction, distance, color = instruction
    hex_distance = color[:-1]
    direction_code = int(color[-1])
    direction = "RDLU"[direction_code]
    distance = int(hex_distance, 16)
    new_instructions.append((direction, distance))

print(get_area(new_instructions))

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

corner_pairs = {
    "F7": ((-0.5, 0.5), (0.5, 0.5)),
    "FL": ((-0.5, 0.5), (-0.5, -0.5)),
    "FJ": ((-0.5, 0.5), (-0.5, 0.5)),
    "7L": ((0.5, 0.5), (0.5, 0.5)),
    "7J": ((0.5, 0.5), (0.5, -0.5)),
    "7F": ((0.5, 0.5), (-0.5, 0.5)),
    "LJ": ((-0.5, -0.5), (0.5, -0.5)),
    "LF": ((-0.5, -0.5), (-0.5, 0.5)),
    "L7": ((-0.5, -0.5), (0.5, 0.5)),
    "JF": ((0.5, -0.5), (0.5, -0.5)),
    "J7": ((0.5, -0.5), (0.5, 0.5)),
    "JL": ((0.5, -0.5), (-0.5, -0.5)),
}


def parse_instruction(line):
    direction, distance, color = line.strip().split()
    color = color[2:-1]
    return direction, int(distance), color


instructions = [parse_instruction(line) for line in lines]

vertex = (0, 0)
vertices = []
for i, (direction, dist, color) in enumerate(instructions):
    d = directions[direction]
    next_direction, next_dist, next_color = instructions[(i + 1) % len(instructions)]
    print(direction, next_direction, vertex)
    corner_type = direction_pairs[direction + next_direction]
    vertex = (vertex[0] + d[0] * dist, vertex[1] + d[1] * dist, corner_type)
    vertices.append(vertex)

print(vertices)

# def intersect(pair1, pair2):
#     x1, x2 = pair1
#     x3, x4 = pair2
#     if x3 <= x1 <= x4 or x1 <= x3 <= x2:
#         return True
#     return False


# def make_pairs(xs):
#     pairs = []
#     i = 0
#     while i < len(xs) - 1:
#         pairs.append((xs[i], xs[i + 1]))
#         i += 2
#     return pairs


# ys = sorted(set([v[1] for v in vertices]), reverse=True)
# prev_xs = []
# prev_length = 0
# prev_pairs = []
# area = 0
# for i, y in enumerate(ys[:-1]):
#     xs = [v[0] for v in vertices if v[1] == y]
#     carry_over = [x for x in prev_xs if x not in xs]
#     new = [x for x in xs if x not in prev_xs]
#     xs = sorted(set(carry_over + new))
#     x_pairs = make_pairs(xs)
#     intersecting_pairs = [
#         [(pair, prev_pair) for prev_pair in prev_pairs if intersect(pair, prev_pair)]
#         for pair in x_pairs
#     ]
#     # flatten intersecting_pairs
#     intersecting_pairs = set([pair for pairs in intersecting_pairs for pair in pairs])
#     expanded_intersecting_pairs = [
#         (min(a[0], b[0]), max(a[1], b[1])) for a, b in intersecting_pairs
#     ]
#     current_intersecting_pairs = [pair[0] for pair in intersecting_pairs]
#     non_intersecting_pairs = [
#         pair for pair in x_pairs if pair not in current_intersecting_pairs
#     ]
#     current_line_length = sum(
#         [x2 - x1 + 1 for x1, x2 in expanded_intersecting_pairs]
#     ) + sum([x2 - x1 + 1 for x1, x2 in non_intersecting_pairs])
#     length = sum([x2 - x1 + 1 for x1, x2 in x_pairs])
#     height = abs(y - ys[i + 1]) - 1
#     area += length * height
#     if i == len(ys) - 2:
#         area += length
#     if i == 0:
#         area += length
#     else:
#         area += current_line_length
#     print(
#         y,
#         x_pairs,
#         length,
#         current_intersecting_pairs,
#         non_intersecting_pairs,
#         current_line_length,
#         area,
#     )
#     prev_xs = xs
#     prev_pairs = x_pairs
#     prev_length = length

# print(area)

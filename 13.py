import itertools


with open("input/13.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# group lines separated by empty lines
groups = []
group = []
for line in lines:
    if line == "":
        groups.append(group)
        group = []
    else:
        group.append(line)
if len(group) > 0:
    groups.append(group)


def to_column_group(group):
    column_group = []
    for i in range(len(group[0])):
        column = [line[i] for line in group]
        column_group.append(column)
    return column_group


def find_reflection_points(group):
    i = 1
    reflection_points = []
    while i < len(group):
        if group[i] == group[i - 1]:
            reached_end = False
            j = 0
            while not reached_end:
                j += 1
                if i + j >= len(group):
                    reached_end = True
                    break
                if i - j - 1 < 0:
                    reached_end = True
                    break
                if group[i + j] != group[i - j - 1]:
                    break
            if reached_end:
                reflection_points.append(i)
        i += 1
    return reflection_points


def get_reflection_types(group):
    horizontal_reflections = find_reflection_points(group)
    column_group = to_column_group(group)
    vertical_reflections = find_reflection_points(column_group)
    reflection_types = []
    for reflection_point in horizontal_reflections:
        reflection_types.append(("horizontal", reflection_point))
    for reflection_point in vertical_reflections:
        reflection_types.append(("vertical", reflection_point))
    return reflection_types


sum = 0
for group in groups:
    reflection_type, reflection_point = get_reflection_types(group)[0]
    if reflection_type == "vertical":
        sum += reflection_point
    elif reflection_type == "horizontal":
        sum += reflection_point * 100

print(sum)


def smudge(group, i, j):
    new_group = []
    for x in range(len(group)):
        if x != i:
            new_group.append(group[x])
            continue
        new_line = ""
        for y in range(len(group[0])):
            c = group[x][y]
            if y != j:
                new_line += c
                continue
            new_line += "." if c == "#" else "#"
        new_group.append(new_line)
    return new_group


def find_smudge(group):
    reflection_types = get_reflection_types(group)
    for i in range(len(group)):
        for j in range(len(group[0])):
            smudged_group = smudge(group, i, j)
            smudged_reflection_types = get_reflection_types(smudged_group)
            for reflection_type in smudged_reflection_types:
                if reflection_type not in reflection_types:
                    return i, j, reflection_type

    return None


sum = 0
for group in groups:
    i, j, reflection_type = find_smudge(group)
    type, reflection_point = reflection_type
    if type == "vertical":
        sum += reflection_point
    elif type == "horizontal":
        sum += reflection_point * 100

print(sum)

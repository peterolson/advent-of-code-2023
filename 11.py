with open("input/11.txt", "r") as f:
    lines = f.readlines()

map = [[c for c in line.strip()] for line in lines]

def is_row_empty(i):
    return all([map[i][j] == "." for j in range(len(map[i]))])

def is_col_empty(j):
    return all([map[i][j] == "." for i in range(len(map))])

empty_rows = [i for i in range(len(map)) if is_row_empty(i)]
empty_cols = [j for j in range(len(map[0])) if is_col_empty(j)]

galaxy_locations = [(i, j) for i in range(len(map)) for j in range(len(map[i])) if map[i][j] == "#"]

def distance_between_galaxies(g1, g2, empty_distance):
    g1_i, g1_j = g1
    g2_i, g2_j = g2
    horizontal_distance = abs(g1_j - g2_j)
    vertical_distance = abs(g1_i - g2_i)
    # add 1 for each empty row/col between the two galaxies
    for i in range(min(g1_i, g2_i) + 1, max(g1_i, g2_i)):
        if i in empty_rows:
            vertical_distance += empty_distance - 1
    for j in range(min(g1_j, g2_j) + 1, max(g1_j, g2_j)):
        if j in empty_cols:
            horizontal_distance += empty_distance - 1
    return horizontal_distance + vertical_distance

galaxy_pairs = [(g1, g2) for g1 in galaxy_locations for g2 in galaxy_locations if g1 < g2]
galaxy_distances = [distance_between_galaxies(g1, g2, 2) for g1, g2 in galaxy_pairs]

print(sum(galaxy_distances))

galaxy_distances = [distance_between_galaxies(g1, g2, 1000000) for g1, g2 in galaxy_pairs]

print(sum(galaxy_distances))
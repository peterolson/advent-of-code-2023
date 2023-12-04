import math

with open('input/2.txt', 'r') as f:
    lines = f.readlines()

def parse_line(line):
    [id_part, sets_part] = line.split(":")
    game_id = int(id_part.split(" ")[1])
    set_parts = [set_part.strip().split(", ") for set_part in sets_part.split(";")]
    def parse_items(set_part):
        [n, color] = set_part.split(" ")
        return (int(n), color)
    set_parts = [[parse_items(items) for items in set_part] for set_part in set_parts]
    return (game_id, set_parts)

bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def is_possible(sets):
    for set in sets:
        for (n, color) in set:
            if bag[color] < n:
                return False
    return True

games = [parse_line(line) for line in lines]
possible_games = [game_id for (game_id, sets) in games if is_possible(sets)]
print(f"Part 1: {sum(possible_games)}")

def get_power(game):
    (game_id, sets) = game
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set in sets:
        for (n, color) in set:
            mins[color] = max(mins[color], n)
    return math.prod(mins.values())

powers = [get_power(game) for game in games]
print(f"Part 2: {sum(powers)}")
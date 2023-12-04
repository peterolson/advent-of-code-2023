import math

with open("input/4.txt", "r") as f:
    lines = f.readlines()


def parse_line(line):
    [id_part, numbers_part] = line.split(": ")
    card_id = int(id_part[5:])
    [winning_numbers, numbers_had] = numbers_part.split(" | ")
    winning_numbers = [int(x) for x in winning_numbers.split()]
    numbers_had = [int(x) for x in numbers_had.split()]
    return (card_id, winning_numbers, numbers_had)


def get_matches_count(card):
    (card_id, winning_numbers, numbers_had) = card
    winning_numbers_had = [x for x in numbers_had if x in winning_numbers]
    return len(winning_numbers_had)


def get_points(card):
    return math.floor(2 ** (get_matches_count(card) - 1))


cards = [parse_line(line) for line in lines]
points = [get_points(card) for card in cards]

print(f"Part 1: {sum(points)}")

card_instances = [1 for card in cards]

for i, card in enumerate(cards):
    instances = card_instances[i]
    matches_count = get_matches_count(card)
    for j in range(matches_count):
        card_instances[i + j + 1] += instances

print(f"Part 2: {sum(card_instances)}")

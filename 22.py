import argparse
from collections import defaultdict
import re


Brick = tuple[tuple[int, int, int], tuple[int, int, int]]
Point = tuple[int, int]


def part_one(lines: list[str]) -> int:
    bricks: list[Brick] = []
    for line in lines:
        x1, y1, z1, x2, y2, z2 = re.findall(
            "(\\d+),(\\d+),(\\d+)~(\\d+),(\\d+),(\\d+)", line
        )[0]
        bricks.append(((int(x1), int(y1), int(z1)), (int(x2), int(y2), int(z2))))

    # (x, y): (max_height, brick_ix) where brick_ix of -1 indicates the floor
    height_map: defaultdict[Point, Point] = defaultdict(lambda: (0, -1))
    supports: defaultdict[int, set[int]] = defaultdict(set)  # brick_ix: {supported_ix,}
    supported_by: dict[int, set[int]] = {}  # brick_ix: {supported_by_ix,}

    bricks.sort(key=lambda b: min(b[0][2], b[1][2]))
    for ix, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        z_min = min(z1, z2)
        z_max = max(z1, z2)

        max_height = 0
        brick_supported_by: set[int] = set()
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                height, brick_ix = height_map[(x, y)]
                if height > max_height:
                    max_height = height
                    brick_supported_by = set([brick_ix])
                elif height == max_height:
                    brick_supported_by.add(brick_ix)

        for i in brick_supported_by:
            supports[i].add(ix)
        supported_by[ix] = brick_supported_by

        dz = z_min - max_height - 1
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                height_map[(x, y)] = (z_max - dz, ix)

    disintegrate_count = 0
    for ix in range(len(bricks)):
        for supported_ix in supports[ix]:
            if len(supported_by[supported_ix]) == 1:
                break
        else:
            disintegrate_count += 1

    return disintegrate_count


def part_two(lines: list[str]) -> int:
    bricks: list[Brick] = []
    for line in lines:
        x1, y1, z1, x2, y2, z2 = re.findall(
            "(\\d+),(\\d+),(\\d+)~(\\d+),(\\d+),(\\d+)", line
        )[0]
        bricks.append(((int(x1), int(y1), int(z1)), (int(x2), int(y2), int(z2))))

    # (x, y): (max_height, brick_ix) where brick_ix of -1 indicates the floor
    height_map: defaultdict[Point, Point] = defaultdict(lambda: (0, -1))
    supports: defaultdict[int, set[int]] = defaultdict(set)  # brick_ix: {supported_ix,}
    supported_by: dict[int, set[int]] = {}  # brick_ix: {supported_by_ix,}

    bricks.sort(key=lambda b: min(b[0][2], b[1][2]))
    for ix, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        z_min = min(z1, z2)
        z_max = max(z1, z2)

        max_height = 0
        brick_supported_by: set[int] = set()
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                height, brick_ix = height_map[(x, y)]
                if height > max_height:
                    max_height = height
                    brick_supported_by = set([brick_ix])
                elif height == max_height:
                    brick_supported_by.add(brick_ix)

        for i in brick_supported_by:
            supports[i].add(ix)
        supported_by[ix] = brick_supported_by

        dz = z_min - max_height - 1
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                height_map[(x, y)] = (z_max - dz, ix)

    total = 0
    for disintegrate_ix in range(len(bricks)):
        will_fall = set([disintegrate_ix])
        for ix in range(disintegrate_ix + 1, len(bricks)):
            if not supported_by[ix] - will_fall:
                will_fall.add(ix)
        total += len(will_fall) - 1

    return total


with open("input/22.txt", "r") as file:
    lines = file.read().splitlines()

print(f"part 1 solution: {part_one(lines)}")
print(f"part 2 solution: {part_two(lines)}")

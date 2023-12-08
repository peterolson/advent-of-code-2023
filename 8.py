from math import lcm

with open("input/8.txt", "r") as f:
    lines = f.readlines()

pattern = lines[0].strip()

nodes = dict()

for line in lines[2:]:
    name, next = line.strip().split(" = ")
    left, right = next.split(", ")
    left = left[1:]
    right = right[:-1]
    nodes[name] = (left, right)

start = 'AAA'
target = 'ZZZ'

current = start
i = 0
while current != target:
    left, right = nodes[current]
    if pattern[i % len(pattern)] == 'L':
        current = left
    else:
        current = right
    i += 1

print(f"Part 1: {i}")

# Part 2

# get nodes with key ending with a
start_nodes = [k for k in nodes.keys() if k[-1] == 'A']

def get_length(start_node):
    current = start_node
    i = 0
    while current[-1] != 'Z':
        left, right = nodes[current]
        if pattern[i % len(pattern)] == 'L':
            current = left
        else:
            current = right
        i += 1
    return i

lengths = [get_length(start_node) for start_node in start_nodes]

print(f"Part 2: {lcm(*lengths)}")
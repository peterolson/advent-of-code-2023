with open("input/15.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def HASH(str):
    c = 0
    for char in str:
        c += ord(char)
        c = (c * 17) % 256
    return c

initialization_sequence = lines[0].split(",")
hashes = [HASH(str) for str in initialization_sequence]
print(sum(hashes))

def parse_command(command):
    if command[-1] == "-":
        return "remove", (command[:-1], HASH(command[:-1]))
    label, value = command.split("=")
    return "push", (label, HASH(label), int(value))

commands = [parse_command(command) for command in initialization_sequence]

boxes = {}
for command in commands:
    type, args = command
    if type == "remove":
        label, box = args
        boxes[box] = boxes.get(box, [])
        boxes[box] = [(l, v) for (l, v) in boxes[box] if l != label]
    else:
        label, box, value = args
        boxes[box] = boxes.get(box, [])
        if label not in [l for (l, v) in boxes[box]]:
            boxes[box].append((label, value))
        else:
            boxes[box] = [(l, v) if l != label else (l, value) for (l, v) in boxes[box]]

focusing_power = 0
for box, lenses in boxes.items():
    for i, (label, value) in enumerate(lenses):
        focusing_power += (box + 1) * (i + 1) * value

print(focusing_power)
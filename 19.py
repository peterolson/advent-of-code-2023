with open("input/19.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def parse_workflow(line):
    name, rule = line.split("{")
    rules = rule[:-1].split(",")
    parsed_rules = []
    for rule in rules:
        if ":" not in rule:
            parsed_rules.append(rule)
            continue
        condition, target = rule.split(":")
        field = condition[0]
        operator = condition[1]
        value = int(condition[2:])
        parsed_rules.append((field, operator, value, target))
    return name, parsed_rules


def parse_part(line):
    stripped = line[1:-1]
    parts = stripped.split(",")
    values = [int(part.split("=")[1]) for part in parts]
    [x, m, a, s] = values
    return {"x": x, "m": m, "a": a, "s": s}


workflows = {}
parts = []
workflows_done = False
for line in lines:
    if line == "":
        workflows_done = True
        continue
    if workflows_done:
        parts.append(parse_part(line))
    else:
        name, workflow = parse_workflow(line)
        workflows[name] = workflow


def execute_workflow(part, workflow):
    for rule in workflow:
        if isinstance(rule, str):
            target = rule
            if target in ["A", "R"]:
                return target
            return execute_workflow(part, workflows[target])
        field, operator, value, target = rule
        a = part[field]
        passes_condition = False
        if operator == "<":
            passes_condition = a < value
        elif operator == ">":
            passes_condition = a > value
        if passes_condition:
            if target in ["A", "R"]:
                return target
            return execute_workflow(part, workflows[target])


accepted_parts = [
    part for part in parts if execute_workflow(part, workflows["in"]) == "A"
]
total_rating = sum(
    [part["x"] + part["m"] + part["a"] + part["s"] for part in accepted_parts]
)
print(total_rating)


def get_ranges(workflow, range):
    all_ranges = []
    current_range = range
    for rule in workflow:
        if isinstance(rule, str):
            if rule in workflows:
                all_ranges += get_ranges(workflows[rule], current_range)
                continue
            elif rule == "A":
                all_ranges.append(current_range)
                continue
            continue
        field, operator, value, target = rule
        lower, upper = current_range[field]
        current_lower, current_upper = current_range[field]
        if operator == "<":
            upper = min(value - 1, upper)
            current_lower = max(value, current_lower)
        elif operator == ">":
            lower = max(value + 1, lower)
            current_upper = min(value, current_upper)
        new_range = {**current_range, field: [lower, upper]}
        current_range = {**current_range, field: [current_lower, current_upper]}
        if target in workflows:
            all_ranges += get_ranges(workflows[target], new_range)
        elif target == "A":
            all_ranges.append(new_range)

    return all_ranges


def get_size(range):
    size = 1
    for key in range:
        lower, upper = range[key]
        if lower > upper:
            return 0
        size *= upper - lower + 1
    return size


ranges = get_ranges(
    workflows["in"], {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
)

sets = [{i} for i in range(len(ranges))]

total = 0
for range in ranges:
    total += get_size(range)

print(total)

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
    [x,m,a,s] = values
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

accepted_parts = [part for part in parts if execute_workflow(part, workflows["in"]) == "A"]
total_rating = sum([part["x"] + part["m"] + part["a"] + part["s"] for part in accepted_parts])
print(total_rating)

def get_ranges(workflow, range):
    accepted_ranges = []
    current_range = range
    for rule in workflow:
        if isinstance(rule, str):
            if rule == "A":
                accepted_ranges.append(current_range)
                continue
            elif rule == "R":
                continue
            elif rule in workflows:
                accepted_ranges += get_ranges(workflows[rule], current_range)
                continue
        field, operator, value, target = rule
        lower, upper = current_range[field]
        if operator == "<":
            upper = min(value - 1, upper)
        elif operator == ">":
            lower = max(value + 1, lower)
        new_range = {**current_range, field: [lower, upper]}
        if target == "A":
            accepted_ranges.append(new_range)
        elif target == "R":
            continue
        elif target in workflows:
            accepted_ranges += get_ranges(workflows[target], new_range)
                
    return accepted_ranges

def get_intersection(ranges):
    intersection = {}
    for range in ranges:
        for field in ["x", "m", "a", "s"]:
            if field not in intersection:
                intersection[field] = range[field]
            else:
                lower, upper = intersection[field]
                new_lower, new_upper = range[field]
                intersection[field] = [max(lower, new_lower), min(upper, new_upper)]
    total_possibilities = 1
    for field in ["x", "m", "a", "s"]:
        lower, upper = intersection[field]
        if lower > upper:
            return 0
        total_possibilities *= (upper - lower + 1)
    return total_possibilities

def is_entailed_by(range1, range2):
    for field in ["x", "m", "a", "s"]:
        lower1, upper1 = range1[field]
        lower2, upper2 = range2[field]
        if lower1 < lower2 or upper1 > upper2:
            return False
    return True

def deduplicate(list_of_sets : list[set]):
    encountered = set()
    deduplicated = []
    for s in list_of_sets:
        key = tuple(sorted(s))
        if key not in encountered:
            encountered.add(key)
            deduplicated.append(s)
    return deduplicated
    
ranges = get_ranges(workflows["in"], {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]})

current_iteration = [{i} for i in range(len(ranges))]
sign = 1
sum = 0
while len(current_iteration) > 0:
    non_empty = []
    for group in current_iteration:
        intersection = get_intersection([ranges[i] for i in group])
        if intersection == 0:
            continue
        sum += sign * intersection
        non_empty.append(group)
    next_iteration = []
    for group in non_empty:
        group_max = max(group)
        next_items = [i for i in range(len(ranges)) if i not in group]
        for item in next_items:
            next_iteration.append(group.union({item}))
    next_iteration = deduplicate(next_iteration)
    # remove duplicates
    print(next_iteration)
    sign *= -1
    current_iteration = next_iteration
    print(len(current_iteration), sum)
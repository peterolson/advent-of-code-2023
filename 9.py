with open("input/9.txt", "r") as f:
    lines = f.readlines()

lines = [[int(x) for x in line.strip().split()] for line in lines]

def get_differences(nums):
    return [nums[i+1] - nums[i] for i in range(len(nums)-1)]

def all_zeroes(nums):
    return all([x == 0 for x in nums])

def extrapolate(nums):
    steps = [nums]
    while not all_zeroes(steps[-1]):
        steps.append(get_differences(steps[-1]))
    next_num = sum([step[-1] for step in steps])
    return next_num

print(sum([extrapolate(line) for line in lines]))

def extrapolate_steps(nums):
    steps = [nums]
    while not all_zeroes(steps[-1]):
        steps.append(get_differences(steps[-1]))
    next_num = 0
    i = len(steps) - 1
    while i >= 0:
        next_num = steps[i][0] - next_num
        i -= 1
    return next_num

print(sum([extrapolate_steps(line) for line in lines]))
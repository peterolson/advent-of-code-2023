import re

lines = []
with open('input/1.txt', 'r') as f:
    lines = f.readlines()

# Part 1

numeric_chars = [[char for char in line if char.isdigit()] for line in lines]
calibration_values = [int(line[0] + line[-1]) for line in numeric_chars]
print(f"Part 1: {sum(calibration_values)}")

# Part 2

pattern = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))' # Lookahead to allow overlapping matches
            # Idea from https://stackoverflow.com/questions/5616822/how-to-use-regex-to-find-all-overlapping-matches
word_to_number = {
    'one': "1", 'two': "2", 'three': "3", 'four': "4", 'five': "5",
    'six': "6", 'seven': "7", 'eight':"8", 'nine': "9"
}

def to_list_of_numbers(line):
    matches = re.findall(pattern, line)
    return [word_to_number[match] if match in word_to_number else match for match in matches]

numeric_parts = [to_list_of_numbers(line) for line in lines]
calibration_values = [int(parts[0] + parts[-1]) for parts in numeric_parts]
print(f"Part 2: {sum(calibration_values)}")
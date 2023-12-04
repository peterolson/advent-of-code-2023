with open('input/3.txt', 'r') as f:
    lines = f.readlines()

numbers = []
symbols = []

for i, line in enumerate(lines):
    chars = line.strip()
    current_number = ''
    current_number_start = None
    for j, char in enumerate(chars):
        if char.isdigit():
            if not current_number:
                current_number_start = j
            current_number += char
            continue
        if current_number:
            numbers.append((i, current_number_start, j, int(current_number)))
            current_number = ''
        if char != '.':
            symbols.append((i, j, char))
    if current_number:
        numbers.append((i, current_number_start, j + 1, int(current_number)))

def is_adjacent(number, symbol):
    (s_i, s_j, s_char) = symbol
    (n_i, n_start, n_end, n_number) = number
    return n_i - 1 <= s_i <= n_i + 1 and n_start - 1 <= s_j <= n_end

def is_adjacent_to_any(number):
    for symbol in symbols:
        if is_adjacent(number, symbol):
            return True
    return False


numbers_with_adjacent_symbols = [number[3] for number in numbers if is_adjacent_to_any(number)]
print(f"Part 1: {sum(numbers_with_adjacent_symbols)}")

def get_adjacent_numbers(symbol):
    return [number for number in numbers if is_adjacent(number, symbol)]
    
potential_gears = [(symbol, get_adjacent_numbers(symbol)) for symbol in symbols if symbol[2] == '*']
gears = [gear for gear in potential_gears if len(gear[1]) == 2]
gear_ratios = [gear[1][0][3] * gear[1][1][3] for gear in gears]

print(f"Part 2: {sum(gear_ratios)}")
import regex

def main():
    with open("input.txt", "r") as f:
        print(part_two([lines.strip() for lines in f.readlines()]))

def part_one(f):
    lines = enumerate(f)
    parts_arr = []
    sum = 0
    for index, line in lines:
        numbers = regex.findall(r'(\d+)', line)
        for match in numbers:
            parts_arr.append({
                'row': index,
                'start': regex.search(r'\b'+match+r'\b', line).start(),
                'end': regex.search(r'\b'+match+r'\b', line).end(),
                'value': match
            })

    print(parts_arr)
    non_parts = []
    parts = []
    for part in parts_arr:
        if validate_part_number(part, f):
            parts.append(part)
            sum += int(part['value'])
        else:
            non_parts.append(part)

    for part in parts:
        print(part)

    return sum
def validate_part_number(part_obj, lines):
    xy_pairs_up = [(part_obj['row']-1, x) for x in range(part_obj['start']-1, part_obj['end']+1)]
    xy_pairs_med = [(part_obj['row'], x) for x in range(part_obj['start']-1, part_obj['end']+1)]
    xy_pairs_down = [(part_obj['row']+1, x) for x in range(part_obj['start']-1, part_obj['end']+1)]
    full_coords = []
    full_coords.extend(xy_pairs_up)
    full_coords.extend(xy_pairs_med)
    full_coords.extend(xy_pairs_down)
    print(full_coords)
    for coords in full_coords:
        try:
            if not lines[coords[0]][coords[1]].isdigit() and lines[coords[0]][coords[1]] != '.' and coords[0] >= 0 and coords[1] >= 0:
                print(coords, lines[coords[0]][coords[1]])
                return True
        except IndexError:
            pass
    return False


#Failed part two, need to start from a new paradigm. Extending part one was unsuccessful--unclear how to prevent matching the same number twice
def part_two(f):
    parts_arr = []
    for index, line in enumerate(f):
        numbers = regex.finditer(r'\b(?P<value>\d+)\b', line)
        for match in numbers:
            parts_arr.append({
                'coords': [(index, x) for x in range(match.start(), match.end())],
                'value': match.group('value')
            })
    gears = []
    for index, line in enumerate(f):
        for char_ind in range(len(line)):
            if line[char_ind] == '*':
                xy_pairs_up = [(index - 1, x) for x in range(char_ind - 1, char_ind + 2)]
                xy_pairs_med = [(index, x) for x in range(char_ind - 1, char_ind + 2)]
                xy_pairs_down = [(index + 1, x) for x in range(char_ind - 1, char_ind + 2)]
                check_coords = []
                check_coords.extend(xy_pairs_up)
                check_coords.extend(xy_pairs_med)
                check_coords.extend(xy_pairs_down)
                gears.append({
                    'loc': (index, char_ind),
                    'checks': check_coords
                })

    sum = 0
    for gear in gears:
        sum += gear_checker(gear, parts_arr, f)
    return sum

def gear_checker(gear, parts, lines):
    values = []
    try:
        for coordinate in gear['checks']:
            print(coordinate)
            if lines[coordinate[0]][coordinate[1]].isdigit():
                for part in parts:
                    if coordinate in part['coords'] and {'coords': part['coords'], 'value': part['value']} not in values:
                        print(part)
                        values.append({'coords': part['coords'], 'value': part['value']})
    except:
        pass
    if len(values) == 2:
        print(values)
        return int(values[0]['value']) * int(values[1]['value'])
    return 0



if __name__ == "__main__":
    main()
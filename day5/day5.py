import regex

def main():
    with open("input.txt", "r") as f:
        print(part_one([lines.strip() for lines in f.readlines()]))
'''
def part_one(f):
    map_dict = map_const(f)
    seed_journeys = []
    for seed in [int(x) for x in f[0].replace('seeds: ', '').split()]:
        source = seed
        journey = []
        for key in map_dict:
            try:
                coord = [x for x in map_dict[key] if x[0] == source][0]
                journey.append(coord)
                source = coord[1]
            except IndexError:
                journey.append((source, source))
        seed_journeys.append(journey)
    return seed_journeys

'''
def map_const(f):
    current_mapping = ''
    map_dict = {
        'seed-to-soil': [],
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': []
    }

    for line in f[2:]:
        if ":" in line:
            current_mapping = line.replace(' map:', '').strip()
        elif line == "":
            pass
        else:
            map_dict[current_mapping].append(line.split())
    return map_dict


def part_one(f):
    map_dict = map_const(f)
    seeds = [int(x) for x in f[0].replace('seeds: ', '').split()]
    seed_pairs = []
    location_arr = []
    guess_number = 36471856340000
    for pair in range(1, len(seeds), 2):
        seed_pairs.append((int(seeds[pair-1]), int(seeds[pair])))

    for pair in seed_pairs:
        print(pair)
        for seed_start in range(pair[0], pair[0]+pair[1], 1):
            location = location_finder(seed_start, map_dict)
            if location < guess_number:
                guess_number = location
    return guess_number

def location_finder(seed, map_dict):
    current_value = seed
    for key in map_dict:
        for line in map_dict[key]:
            if int(line[1]) <= current_value <= (int(line[1]) + int(line[2])):
                current_value = int(line[0]) + (current_value - int(line[1]))
                break
    return current_value


def part_two(f):
    return f

if __name__ == "__main__":
    main()
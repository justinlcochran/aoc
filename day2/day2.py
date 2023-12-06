import regex

def main():
    with open("input.txt", "r") as f:
        print(part_two(f))

def part_one(f):
    lines = f.readlines()
    sum = 0
    for line in lines:
        red = max([int(x) for x in regex.findall(r'(\d+) red', line)])
        green = max([int(x) for x in regex.findall(r'(\d+) green', line)])
        blue = max([int(x) for x in regex.findall(r'(\d+) blue', line)])
        if red <= 12 and green <= 13 and blue <= 14:
            sum += int(regex.findall(r'Game (\d+):', line)[0])
    return sum

def part_two(f):
    lines = f.readlines()
    sum = 0
    for line in lines:
        red = max([int(x) for x in regex.findall(r'(\d+) red', line)])
        green = max([int(x) for x in regex.findall(r'(\d+) green', line)])
        blue = max([int(x) for x in regex.findall(r'(\d+) blue', line)])
        sum += red * green * blue
    return sum

if __name__ == "__main__":
    main()
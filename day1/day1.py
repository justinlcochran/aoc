import regex

def main():
    with open("input.txt", "r") as f:
        print(part_two(f))

def part_one(f):
    sum = 0
    for line in f.readlines():
        num_arr = [char for char in line if char.isdigit()]
        sum += int(f"{num_arr[0]}{num_arr[-1]}")
    return sum
    #correct

def part_two(f):
    number_dict = {
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9",
    }

    sum = 0
    lines = f.readlines()
    new_lines = []
    for line in lines:
        numbers = regex.findall(r'(one|two|three|four|five|six|seven|eight|nine|[0-9])', line, overlapped=True)
        print(numbers)
        if not numbers[0].isdigit():
            first_digit = number_dict[numbers[0]]
        else:
            first_digit = numbers[0]

        if not numbers[-1].isdigit():
            last_digit = number_dict[numbers[-1]]
        else:
            last_digit = numbers[-1]
        sum += int(f"{first_digit}{last_digit}")

    return sum


if __name__ == "__main__":
    main()
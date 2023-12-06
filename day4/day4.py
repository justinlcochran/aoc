
def main():
    with open("input.txt", "r") as f:
        print(part_two([lines.strip() for lines in f.readlines()]))

def part_one(f):
    sum = 0
    for line in f:
        sum += cruncher(line)
    return sum

def part_two(f):
    card_objects = []

    for line in f:
        title, numbers = line.split(':')
        winners, entries = numbers.split('|')
        winners = winners.split()
        entries = entries.split()
        card_objects.append({
            'card_number': int(title.split()[1]),
            'winners': winners,
            'entries': entries,
            'count': 1
        })
    for index, card in enumerate(card_objects):
        for changer in card_objects[index+1:index+cruncher2(card)+1]:
            changer['count'] += card['count']
    sum = 0
    for card in card_objects:
        sum += card['count']
    return sum


def cruncher(line):
    title, numbers = line.split(':')
    winners, entries = numbers.split('|')
    winners = winners.split()
    entries = entries.split()
    count = 0
    for number in entries:
        if number in winners:
            count += 1
    if count > 0:
        return 2 ** (count - 1)
    else:
        return 0

def cruncher2(card):
    count = 0
    for number in card['entries']:
        if number in card['winners']:
            count += 1
    return count


if __name__ == "__main__":
    main()
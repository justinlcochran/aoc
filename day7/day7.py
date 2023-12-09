
def main():
    with open('input.txt', 'r') as f:
        print(part_one([x.strip() for x in f.readlines()]))


def part_one(f):

    hand_type_dict = {
        'five': [],
        'four': [],
        'full_house': [],
        'three': [],
        'two_pair': [],
        'pair': [],
        'high': []
    }

    transformer = {
        'A': 'A',
        'K': 'B',
        'Q': 'C',
        'J': 'D',
        'T': 'E',
        '9': 'F',
        '8': 'G',
        '7': 'H',
        '6': 'I',
        '5': 'J',
        '4': 'K',
        '3': 'L',
        '2': 'M'
    }
    for hand in f:
        new_hand = ''.join([transformer[char] for char in hand.split()[0]])
        hand_type_dict[hand_reader(hand)].append(new_hand+' '+hand.split()[1])

    hands = []
    for key in hand_type_dict:
        for hand in sorted(hand_type_dict[key]):
            hands.append(hand)
    hands = hands[::-1]
    sum = 0
    for i, hand in enumerate(hands):
        sum += (i + 1) * int(hand.split()[1])
    return sum


def hand_reader(hand):
    counter = {char: 0 for char in 'AKQJT98765432'}
    for card in hand.split()[0]:
        counter[card] += 1
    print(counter.values())
    if 5 in counter.values():
        return 'five'
    elif 4 in counter.values():
        return 'four'
    elif 3 in counter.values() and 2 in counter.values():
        return 'full_house'
    elif 3 in counter.values() and 2 not in counter.values():
        return 'three'
    elif 2 in counter.values() and list(counter.values()).count(2) == 2:
        return 'two_pair'
    elif 2 in counter.values():
        return 'pair'
    else:
        return 'high'



def part_two(f):
    return 0


if __name__ == "__main__":
    main()

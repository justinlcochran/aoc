
def main():
    with open('input.txt', 'r') as f:
        print(part_two([x.strip() for x in f.readlines()]))


def part_one(f):
    times, distances = [x.split() for x in f]
    point_arrs = []
    for i in range(1, len(times)):
        point_arrs.append(point_const(int(times[i]), int(distances[i])))

    product = 1
    for arr in point_arrs:
        product *= len(arr)
    return product

def part_two(f):
    time, distance = [int(x.split(':')[1].replace(' ', '')) for x in f]
    print(time, distance)

    points_arr = []
    for i in range(time):
        if i * (time - i) > distance:
            points_arr.append(i)
            break
    for i in range(time, 0, -1):
        if i * (time - i) > distance:
            points_arr.append(i)
            break
    return points_arr[1] - points_arr[0] + 1

def point_const(time, distance):
    points = []
    for i in range(time):
        if i * (time - i) > distance:
            points.append((i, i*(time - i)))
    return points

if __name__ == "__main__":
    main()

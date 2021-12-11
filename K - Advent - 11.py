import numpy as np


def valid(octopuses, point):
    return 0 <= point[0] < octopuses.shape[0] and 0 <= point[1] < octopuses.shape[1]


def adjacent_cells(octopuses, point):
    adjecent = np.array(
        [
            np.subtract(point, (1, 1)),
            np.subtract(point, (-1, -1)),
            np.subtract(point, (1, -1)),
            np.subtract(point, (-1, 1)),
            np.subtract(point, (0, -1)),
            np.subtract(point, (0, 1)),
            np.subtract(point, (-1, 0)),
            np.subtract(point, (1, 0))
        ]
    )

    return list(filter(lambda x: valid(octopuses, x), adjecent))


def flash(octopuses, point):
    octopuses[point[0]][point[1]] = 11

    for p in adjacent_cells(octopuses, point):
        if octopuses[p[0]][p[1]] <= 9:
            octopuses[p[0]][p[1]] += 1

    return


def part1(octopuses):
    flashes = 0

    for _ in range(100):
        octopuses += 1

        overflashes = len(octopuses == 10)

        while overflashes > 0:
            for point in np.argwhere(octopuses == 10):
                flash(octopuses, point)
            
            overflashes = len(octopuses[octopuses == 10])

        flashes += len(octopuses[octopuses > 9])

        octopuses[octopuses > 9] = 0

    return flashes


def part2(octopuses):
    days = 0

    
    while np.sum(octopuses == 0) < 100:
        octopuses += 1

        overflashes = len(octopuses == 10)

        while overflashes > 0:
            for point in np.argwhere(octopuses == 10):
                flash(octopuses, point)
            
            overflashes = len(octopuses[octopuses == 10])


        octopuses[octopuses > 9] = 0

        days += 1

    return days


def main():
    octopuses, octoDays = np.genfromtxt("K - inputs.txt", delimiter=1), np.genfromtxt("K - inputs.txt", delimiter=1)

    print(f'PART 1 - {part1(octopuses)}')
    print(f'PART 2 - {part2(octoDays)}')


if __name__ == '__main__':
    main()

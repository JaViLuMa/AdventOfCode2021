import statistics


def part1(crabs):
  median = statistics.median(crabs)

  total = 0

  for x in crabs:
    total += abs(x - median)

  return int(total)


def part2(crabs):
  average = int(statistics.mean(crabs)) # Round here sucks for some reason

  total = 0

  for x in crabs:
    value = abs(x - average)
    total += value * (value + 1) // 2

  return total


def main():
  with open('G - inputs.txt') as f:
    crabs = list(map(int, f.read().split(',')))

  print(f'PART 1 - {part1(crabs)}')
  print(f'PART 2 - {part2(crabs)}')


if __name__ == "__main__":
  main()

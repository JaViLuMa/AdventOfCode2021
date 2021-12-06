def part2(lanterns):
  fishes = [0] * 9

  for x in lanterns:
    fishes[x] += 1

  for x in range(256):
    fishes = fishes[1:] + fishes[:1]
    fishes[6] += fishes[8]

  return sum(fishes)


def part1(lanterns):
  days = 0

  while days != 80:
    x = 0
    length = len(lanterns)

    while x < length:
      if lanterns[x] == 0:
        lanterns[x] = 6
        lanterns.append(8)
        x += 1
      
      else:
        lanterns[x] -= 1
        x += 1
    
    days += 1

  return len(lanterns)


def main():
  with open('F - inputs.txt') as f:
    lanterns = list(map(int, f.read().split(',')))
    print(f'PART 1 - {part1(lanterns)}')

  with open('F - inputs.txt') as f:
    lanterns = list(map(int, f.read().split(',')))
    print(f'PART 2 - {part2(lanterns)}')


if __name__ == "__main__":
  main()

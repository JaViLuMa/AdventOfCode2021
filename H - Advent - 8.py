def part1(outputs):
  total = 0
  
  for digit in outputs:
    for segment in digit:
      if len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7:
        total += 1

  return total


def part2(lines):
  total = 0

  for part in lines:
    inputs = part.split('|')[0].strip().split()
    outputs = part.split('|')[1].strip().split()

    mapping = {
      0: '',
      1: list([l for l in inputs if len(l) == 2][0]),
      2: '',
      3: '',
      4: list([l for l in inputs if len(l) == 4][0]),
      5: '',
      6: '',
      7: list([l for l in inputs if len(l) == 3][0]),
      8: list([l for l in inputs if len(l) == 7][0]),
      9: ''
    }

    for i in inputs:
      if len(i) == 5 and all(x in i for x in mapping[1]):
        mapping[3] = list(i)

    mapping[9] = list(set(mapping[3] + mapping[4]))

    for i in inputs:
      if len(i) == 6 and all(x in i for x in mapping[1]) and not all(x in i for x in mapping[9]):
        mapping[0] = list(i)

    for i in inputs:
      if len(i) == 6 and not all(x in i for x in mapping[0]) and not all(x in i for x in mapping[9]):
        mapping[6] = list(i)

    for i in inputs:
      if len(i) == 5 and not all(x in i for x in mapping[3]) and set(i).issuperset(set(mapping[4]) - set(mapping[1])):
        mapping[5] = list(i)

    for i in inputs:
      if len(i) == 5 and not all(x in i for x in mapping[3]) and not all(x in i for x in mapping[5]):
        mapping[2] = list(i)

    ans = ''

    for digits in outputs:
      for key, value in mapping.items():
        if set(digits) == set(value):
          ans = ans + str(key)

    total += int(ans)

  return total


def main():
  with open('H - inputs.txt') as f:
    lines = f.read().splitlines()

  outputs = [lines[x].split('|')[1].strip().split() for x in range(len(lines))]

  print(f'PART 1 - {part1(outputs)}')
  print(f'PART 2 - {part2(lines)}')


if __name__ == '__main__':
  main()

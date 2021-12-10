from statistics import median

def part1(lines):
  counter = 0

  for x in lines:
    while True:
      if '()' in x:
        x = x.replace('()', '')
      elif '[]' in x:
        x = x.replace('[]', '')

      elif '{}' in x:
        x = x.replace('{}', '')

      elif '<>' in x:
        x = x.replace('<>', '')

      else:
        break

    for y in range(1, len(x)):
      if x[y] == ')':
        if x[y - 1] == '[' or x[y - 1] == '{' or x[y - 1] == '<':
          counter += 3
          break

      if x[y] == ']':
        if x[y - 1] == '(' or x[y - 1] == '{' or x[y - 1] == '<':
          counter += 57
          break

      if x[y] == '}':
        if x[y - 1] == '(' or x[y - 1] == '[' or x[y - 1] == '<':
          counter += 1197
          break

      if x[y] == '>':
        if x[y - 1] == '(' or x[y - 1] == '{' or x[y - 1] == '[':
          counter += 25137
          break

  return counter


def part2(lines):
  vv = []

  for x in lines:
    counter = 0

    while True:
      if '()' in x:
        x = x.replace('()', '')
      elif '[]' in x:
        x = x.replace('[]', '')

      elif '{}' in x:
        x = x.replace('{}', '')

      elif '<>' in x:
        x = x.replace('<>', '')

      else:
        break

    if ')' not in x and '>' not in x and '}' not in x and ']' not in x:
      x = x[::-1]
      for y in range(len(x)):
        if x[y] == '(':
          counter = (counter * 5) + 1
        if x[y] == '[':
          counter = (counter * 5) + 2
        if x[y] == '{':
          counter = (counter * 5) + 3
        if x[y] == '<':
          counter = (counter * 5) + 4

    vv.append(counter)
    
    vv = [vv[x] for x in range(len(vv)) if vv[x] != 0]

    vv = sorted(vv)

  return median(vv)


def main():
  with open('J - inputs.txt') as f:
    lines = f.read().splitlines()

  print(f'PART 1 - {part1(lines)}')
  print(f'PART 2 - {part2(lines)}')


if __name__ == '__main__':
  main()

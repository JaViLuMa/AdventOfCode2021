from collections import deque

def part1(lines):
  lowPoint = []
  
  for x in range(len(lines)):
    check = False

    for y in range(len(lines[x])):
      if x == 0:
        if y == 0:
          if lines[x][y] < lines[x][y + 1] and lines[x][y] < lines[x + 1][y]:
            lowPoint.append(lines[x][y])

        elif y == len(lines[x]) - 1:
          if lines[x][y] < lines[x + 1][y] and lines[x][y] < lines[x][y - 1]:
            lowPoint.append(lines[x][y])

        else:
          if lines[x][y] < lines[x][y - 1] and lines[x][y] < lines[x][y + 1] and lines[x][y] < lines[x + 1][y]:
            lowPoint.append(lines[x][y])

      elif x > 0 and x < len(lines) - 1:     
        if y == 0:
          if lines[x][y] < lines[x][y + 1] and lines[x][y] < lines[x + 1][y] and lines[x][y] < lines[x - 1][y]:
            lowPoint.append(lines[x][y])
          
        elif y == len(lines[x]) - 1:
          if lines[x][y] < lines[x][y - 1] and lines[x][y] < lines[x + 1][y] and lines[x][y] < lines[x - 1][y]:
            lowPoint.append(lines[x][y])

        else:
          if lines[x][y] < lines[x][y + 1] and lines[x][y] < lines[x][y - 1] and lines[x][y] < lines[x + 1][y] and lines[x][y] < lines[x - 1][y]:
            lowPoint.append(lines[x][y])

      else:
        if y == 0:
          if lines[x][y] < lines[x - 1][y] and lines[x][y] < lines[x][y + 1]:
            lowPoint.append(lines[x][y])
          
        elif y == len(lines[x]) - 1:
          if lines[x][y] < lines[x - 1][y] and lines[x][y] < lines[x][y - 1]:
            lowPoint.append(lines[x][y])
        
        else:
          if lines[x][y] < lines[x][y - 1] and lines[x][y] < lines[x][y + 1] and lines[x][y] < lines[x - 1][y]:
            lowPoint.append(lines[x][y])

  total = 0

  for x in lowPoint:
    total += int(x) + 1

  return total

def part2(lines):
  areas = []

  isVisited = set()

  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if (x, y) not in isVisited and lines[x][y] != 9:
        basinSize = 0

        q = deque()
        q.append((x, y))

        while q:
          (x, y) = q.popleft()

          if (x, y) in isVisited:
            continue

          isVisited.add((x, y))

          basinSize += 1

          moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

          for (adjX, adjY) in moves:
            if adjX < 0 or adjX >= len(lines) or adjY < 0 or adjY >= len(lines[x]):
              continue
            else:
              if lines[adjX][adjY] != 9:
                q.append((adjX, adjY))

        areas.append(basinSize)

  return sorted(areas)
  

def main():
  with open('I - inputs.txt') as f:
    lines = f.read().splitlines()

  print(f'PART 1 - {part1(lines)}')

  with open('I - inputs.txt') as f:
    ll = f.read()

  lines = [list(map(int, list(line))) for line in ll.splitlines()]

  pt2 = part2(lines)

  print(f'PART 2 - {pt2[-3] * pt2[-2] * pt2[-1]}')


if __name__ == '__main__':
  main()
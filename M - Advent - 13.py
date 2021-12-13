from itertools import groupby


def part1(lines, maxX, maxY):
  grid = [['.'] * (maxX + 1) for _ in range(maxY + 1)]

  for x in range(len(lines[0])):
    xCoord = lines[0][x][0]
    yCoord = lines[0][x][1]

    grid[yCoord][xCoord] = '#'
      
  axis, value = lines[1][0][0], lines[1][0][1]

  if axis == 'y':
    for y in range(len(grid[value])):
      grid[value][y] = '_'

    half = []

    for x in range(value + 1, len(grid)):
      points = []
      
      for y in range(len(grid[x])):
        points.append(grid[x][y])

      half.append(points)

    half = half[::-1]

    del grid[value:]

    for x in range(value - len(grid), len(grid)):
      for y in range(len(grid[x])):
        try:
          if grid[x][y] != "#" and half[x][y] == '#':
            grid[x][y] = half[x][y]
        except:
          continue

  elif axis == 'x':
    for x in range(len(grid)):
      grid[x][value] = '|'

    half = []

    for x in range(len(grid)):
      points = []

      for y in range(value + 1, len(grid[x])):
        points.append(grid[x][y])

      half.append(points[::-1])

    for x in range(len(grid)):
      del grid[x][value:]

    
    for x in range(len(grid)):
      for y in range(value - len(grid[x]), len(grid[x])):
        try:
          if grid[x][y] != "#" and half[x][y] == '#':
            grid[x][y] = half[x][y]
        except:
          continue

  count = 0

  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y] == '#':
        count += 1

  return count


def part2(lines, maxX, maxY):
  grid = [['.'] * (maxX + 1) for _ in range(maxY + 1)]

  for x in range(len(lines[0])):
    xCoord = lines[0][x][0]
    yCoord = lines[0][x][1]

    grid[yCoord][xCoord] = '#'

  
  for x in range(len(lines[1])):
    axis, value = lines[1][x][0], lines[1][x][1]

    if axis == 'y':
      for y in range(len(grid[value])):
        grid[value][y] = '_'

      half = []

      for x in range(value + 1, len(grid)):
        points = []
        
        for y in range(len(grid[x])):
          points.append(grid[x][y])

        half.append(points)

      half = half[::-1]

      del grid[value:]

      for x in range(value - len(grid), len(grid)):
        for y in range(len(grid[x])):
          try:
            if grid[x][y] != "#" and half[x][y] == '#':
              grid[x][y] = half[x][y]
          except:
            continue

    elif axis == 'x':
      for x in range(len(grid)):
        grid[x][value] = '|'

      half = []

      for x in range(len(grid)):
        points = []

        for y in range(value + 1, len(grid[x])):
          points.append(grid[x][y])

        half.append(points[::-1])

      for x in range(len(grid)):
        del grid[x][value:]

      
      for x in range(len(grid)):
        for y in range(value - len(grid[x]), len(grid[x])):
          try:
            if grid[x][y] != "#" and half[x][y] == '#':
              grid[x][y] = half[x][y]
          except:
            continue


  for row in grid:
    print(*row)


def main():
  with open('M - inputs.txt') as f:
    lines = f.read().splitlines()

  lines = [list(g) for k, g in groupby(lines, key=bool) if k]

  lines[0] = [list(map(int, lines[0][x].split(','))) for x in range(len(lines[0]))]

  lines[1] = [lines[1][x].split(' ') for x in range(len(lines[1]))]
  lines[1] = [lines[1][x][2].split('=') for x in range(len(lines[1]))]
  
  for x in range(len(lines[1])):
    lines[1][x][1] = int(lines[1][x][1])

  maxX = 0
  maxY = 0

  for x in range(len(lines[0])):
    maxX = max(maxX, lines[0][x][0])

  for y in range(len(lines[0])):
    maxY = max(maxY, lines[0][y][1])

  print(f'PART 1 - {part1(lines, maxX, maxY)}')
  print(f'PART 2 - {part2(lines, maxX, maxY)}')


if __name__ == '__main__':
  main()

def part1(lines):
  horVer = []

  for x in range(len(lines)):
    if lines[x][0][0] == lines[x][1][0] or lines[x][0][1] == lines[x][1][1]:
      horVer.append(lines[x])
  
  ocean = [['.'] * 1000 for _ in range(1000)]

  for x in range(len(horVer)):
    x1, x2 = horVer[x][0][0], horVer[x][1][0]
    y1, y2 = horVer[x][0][1], horVer[x][1][1]

    if x1 >= x2:
      x1, x2 = x2, x1

    if y1 >= y2:
      y1, y2 = y2, y1

    if x1 == x2:
      for y in range(y1, y2 + 1):
        if str(ocean[y][x1]).isdigit():
          ocean[y][x1] += 1
        else:
          ocean[y][x1] = 1
    
    elif y1 == y2:
      for x in range(x1, x2 + 1):
        try:  
          if str(ocean[y1][x]).isdigit():
            ocean[y1][x] += 1
          else:
            ocean[y1][x] = 1
        except:
          continue

  total = 0

  for x in range(len(ocean)):
    for y in range(len(ocean[x])):
      if str(ocean[x][y]).isdigit():
        if ocean[x][y] > 1:
          total += 1

  return total


def part2(lines):
  ocean = [['.'] * 1000 for _ in range(1000)]

  for l in range(len(lines)):
    x1, x2 = lines[l][0][0], lines[l][1][0]
    y1, y2 = lines[l][0][1], lines[l][1][1]

    if x1 == x2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        if str(ocean[x1][y]).isdigit():
          ocean[x1][y] += 1
        else:
          ocean[x1][y] = 1
    
    elif y1 == y2:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        if str(ocean[x][y1]).isdigit():
          ocean[x][y1] += 1
        else:
          ocean[x][y1] = 1

    else:
      slope = (y2 - y1) / (x2 - x1)

      if slope == 1 or slope == -1:
        if x1 < x2 and y1 < y2:
          x, y = x1, y1
          
          while x <= x2 and y <= y2:
            if str(ocean[x][y]).isdigit():
              ocean[x][y] += 1
            else:
              ocean[x][y] = 1
            
            x += 1
            y += 1

        elif x1 > x2 and y1 < y2:
          x, y = x1, y1
          
          while x >= x2 and y <= y2:
            if str(ocean[x][y]).isdigit():
              ocean[x][y] += 1
            else:
              ocean[x][y] = 1
            
            x -= 1
            y += 1

        elif x1 < x2 and y1 > y2:
          x, y = x1, y1
          
          while x <= x2 and y >= y2:
            if str(ocean[x][y]).isdigit():
              ocean[x][y] += 1
            else:
              ocean[x][y] = 1
            
            x += 1
            y -= 1

        elif x1 > x2 and y1 > y2:
          x, y = x1, y1
          
          while x >= x2 and y >= y2:
            if str(ocean[x][y]).isdigit():
              ocean[x][y] += 1
            else:
              ocean[x][y] = 1
            
            x -= 1
            y -= 1

  # for row in ocean:
  #   print(*row)

  total = 0

  for x in range(len(ocean)):
    for y in range(len(ocean[x])):
      if str(ocean[x][y]).isdigit():
        if ocean[x][y] > 1:
          total += 1

  return total


def main():
  with open('E - inputs.txt') as f:
    lines = f.read().splitlines()

  lines = [lines[x].split(' -> ') for x in range(len(lines))]

  for x in range(len(lines)):
    for y in range(len(lines[x])):
      lines[x][y] = list(map(int, lines[x][y].split(',')))

  print(f'PART 1 - {part1(lines)}')
  print(f'PART 2 - {part2(lines)}')


if __name__ == "__main__":
  main()

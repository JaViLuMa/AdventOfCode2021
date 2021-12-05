def main():
  with open('B - inputs.txt') as f:
    lines = f.read().splitlines()

# ------------------- 1 ------------------- #
  lines = [lines[x].split() for x in range(len(lines))]

  horizontal = 0
  vertical = 0

  for x in range(len(lines)):
    if lines[x][0] == "forward":
      horizontal += int(lines[x][1])
    elif lines[x][0] == "up":
      vertical -= int(lines[x][1])
    elif lines[x][0] == "down":
      vertical += int(lines[x][1])

  print(f'PART 1 - {horizontal * vertical}')
# ----------------------------------------- #

# ------------------- 2 ------------------- #
  horizontal = 0
  aim = 0
  depth = 0

  for x in range(len(lines)):
    if lines[x][0] == "forward":
      horizontal += int(lines[x][1])
      depth += (aim * int(lines[x][1]))
    elif lines[x][0] == "up":
      aim -= int(lines[x][1])
    elif lines[x][0] == "down":
      aim += int(lines[x][1])

  print(f'PART 2 - {horizontal * depth}')
# ----------------------------------------- #

if __name__ == "__main__":
  main()

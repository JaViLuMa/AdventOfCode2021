def main():
  with open('E - inputs.txt') as f:
    lines = f.read().splitlines()

# ------------------- 1 ------------------- #
  newNum = []

  zeros = 0
  ones = 0

  for x in range(len(lines[0])):
    for y in range(len(lines)):
      if lines[y][x] == '0':
        zeros += 1
      else:
        ones += 1

    if zeros > ones:
      newNum.append('0')
    else:
      newNum.append('1')

    zeros = 0
    ones = 0

  intNewNum = int(''.join(newNum), 2)
  reverseNewNum = int(''.join(newNum).translate(str.maketrans("01","10")), 2)

  print(f'PART 1 - {intNewNum * reverseNewNum}')
# ----------------------------------------- #

# ------------------- 2 ------------------- #
  newNum = []
  oxygen = []
  co2 = []

  zeros = 0
  ones = 0
  bit = 0

  for x in range(1):
    for y in range(len(lines)):
      if lines[y][x] == "0":
        co2.append(lines[y])
      else:
        oxygen.append(lines[y])

  for x in range(1, len(oxygen[0])):
    for y in range(len(oxygen)):
      try:
        if oxygen[y][x] == "0":
          zeros += 1
        else:
          ones += 1
      except:
        continue

    if zeros > ones:
      for z in range(len(oxygen)):
        try:
          if oxygen[z][x] == "1":
            oxygen[z] = "#"
        except:
          continue

    else:
      for z in range(len(oxygen)):
        try:
          if oxygen[z][x] == "0":
            oxygen[z] = "#"
        except:
          continue

    zeros = 0
    ones = 0

  zeros = 0
  ones = 0

  for x in range(1, len(co2[0])):
    for y in range(len(co2)):
      try:
        if co2[y][x] == "0":
          zeros += 1
        else:
          ones += 1
      except:
        continue

    if zeros <= ones:
      for z in range(len(co2)):
        try:
          if co2[z][x] == "1":
            co2[z] = "#"
        except:
          continue

    else:
      for z in range(len(co2)):
        try:
          if co2[z][x] == "0":
            co2[z] = "#"
        except:
          continue
    
    if len([x for x in co2 if not x.startswith('#')]) == 1:
      break

    zeros = 0
    ones = 0

  oxygen = [x for x in oxygen if not x.startswith('#')]
  co2 = [x for x in co2 if not x.startswith('#')]

  intOxygen = int(oxygen[0], 2)
  intCo2 = int(co2[0], 2)

  print(f'PART 2 - {intOxygen * intCo2}')
# ----------------------------------------- #

if __name__ == "__main__":
  main()

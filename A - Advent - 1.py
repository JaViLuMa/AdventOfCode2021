def main():
  with open('A - inputs.txt') as f:
    lines = list(map(int, f.read().splitlines()))

# ------------------- 1 ------------------- #
  counter = 0

  for x in range(1, len(lines)):
    if lines[x - 1] < lines[x]:
      counter += 1

  print(f'PART 1 - {counter}')
# ----------------------------------------- #

# ------------------- 2 ------------------- #
  counter = 0

  for x in range(2, len(lines) - 1):
    if lines[x - 2] + lines[x - 1] + lines[x] < lines[x - 1] + lines[x] + lines[x + 1]:
      counter += 1

  print(f'PART 2 - {counter}')
# ----------------------------------------- #

if __name__ == "__main__":
  main()

def winning(board):
  total = 0

  for x in range(len(board)):
    for y in range(len(board)):
      if board[x][y] != None:
        total += board[x][y]

  return total


def winningBoard(board):
  for x in range(len(board)):
    row = 0
    column = 0

    for y in range(len(board)):
      if board[x][y] == None:
        row += 1
      if board[y][x] == None:
        column += 1

    if row == 5 or column == 5:
      return winning(board)


def part1(picks, boards):
  for n in picks:
    for board in range(len(boards)):
      for rows in range(len(boards[board])):
        for element in range(len(boards[board][rows])):
          if boards[board][rows][element] == n:
            boards[board][rows][element] = None
      
      if winningBoard(boards[board]):
        return winningBoard(boards[board]) * n


def part2(picks, boards):
  endingBoard = 0

  for n in picks:
    for board in range(len(boards)):
      for rows in range(len(boards[board])):
        for element in range(len(boards[board][rows])):
          if boards[board][rows][element] == n:
            boards[board][rows][element] = None
      
      if winningBoard(boards[board]):
        endingBoard = winningBoard(boards[board]) * n

        boards[board] = None

        pass

    while None in boards:
      for p in range(len(boards)):
        if boards[p] == None:
          boards.pop(p)
          break

  return endingBoard


def main():
  with open('D - inputs.txt') as f:
    picks = list(map(int, f.readline().split(',')))

    lines = f.read().splitlines()[1:]
    lines = [list(map(int, lines[x].strip().split())) for x in range(len(lines)) if lines[x] != '']

    boards = [lines[x:x + 5] for x in range(0, len(lines), 5)]

  print(f'PART 1 - {part1(picks, boards)}')
  print(f'PART 2 - {part2(picks, boards)}')


if __name__ == "__main__":
  main()

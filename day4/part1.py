import sys

class Board:
  def __init__(self, board_lines) -> None:
    self.board = [[[int(n), False] for n in line.replace("\n", "").split(" ") if n != ""] for line in board_lines]

  def mark(self, num):
    for i, row in enumerate(self.board):
      for j, (sq_num, marked) in enumerate(row):
        if sq_num == num:
          self.board[i][j][1] = True
          break 

  def row_won(self, row):
    for j, (sq_num, marked) in enumerate(row):
      if not marked:
        return False
    return True
  def col_won(self, col):
    for i in range(len(self.board)):
      if not self.board[i][col][1]:
        return False
    return True

  def has_won(self):
    # iterate rows.
    for row in self.board:
      if self.row_won(row):
        return True

    # iterate columns.
    for j in range(len(self.board[0])):
      if self.col_won(j):
        return True
        
    return False

  def score(self, final_number):
    s = 0
    for row in self.board:
      for num, marked in row:
        if not marked:
          s += num
    
    return s * final_number

  def __repr__(self) -> str:
    for r in self.board:
      for (sq_num, marked) in r:
        markedchar = '\'' if marked else ''
        pr_value = f"{sq_num}{markedchar}".ljust(3)
        print(pr_value, end=" ")
      print("")

def main():
  sequence = [int(l) for l in sys.stdin.readline().split(",")]
  puzzle_input = [l for l in sys.stdin.readlines()]

  # read boards
  boards = [Board(puzzle_input[i+1:i+6]) for i in range(0, len(puzzle_input), 6)]
  # boards[0].mark(22)

  for n in sequence:
    for b in boards:
      b.mark(n)
      if b.has_won():
        # print(b)
        print(b.score(n))
        return

if __name__ == "__main__":
  main()
import sys
from parse import *

def print_matrix(m):
  for row in m:
    for c in row:
      print(c, end="")

    print()
  print(f"h={len(m)}, w={len(m[0])}")

def fold(paper, where):
  x_or_y, xy = where # where is a tuple of the form ('x', num), or ('y', num)
  match x_or_y:
    case "x":
      folded_paper = [["."] * (len(paper[0])//2) for _ in range(len(paper))]
      for 
    case "y":
      folded_paper = [["."] * len(paper[0]) for _ in range(len(paper)//2)]



  return folded_paper


def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  dots = [parse("{:d},{:d}", l) for l in puzzle_input if "fold along" not in l]
  fold_instructions = [parse("fold along {:l}={:d}", l) for l in puzzle_input if "fold along" in l]
  
  # max x and max y
  max_x = max(x for x, y in dots)
  max_y = max(y for x, y in dots)

  # paper is a dot matrix
  paper = [["."] * (max_x + 1) for _ in range(max_y + 1)]
  # fill paper
  for dot in dots:
    dotx, doty = dot
    paper[doty][dotx] = "#"

  print_matrix(paper)
  print()
  paper = fold(paper, ("y", 7))
  print_matrix(paper)

if __name__ == "__main__":
  main()
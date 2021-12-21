import sys
from parse import *

def print_dots(dots):
  width = max(x for x, y in dots) + 1
  height = max(y for x, y in dots) + 1
  
  for y in range(height):
    for x in range(width):
      print("#" if (x, y) in dots else ".", end="")

    print()
  print(f"h={height}, w={width}")

def fold(dots, where):
  coordinate, fold_pos = where # "where" is a tuple of the form ('x', num), or ('y', num)
  folded_dots = []
  # match coordinate:
  #   case "x":

  #   case "y":
  #     folded_dots = []

  for dot in dots:
    dotx, doty = dot
    match coordinate:
      case "y":
        if doty < fold_pos:
          folded_dots.append(dot)
        else:
          folded_dots.append((dotx, fold_pos - (doty - fold_pos)))
      case "x":
        if dotx < fold_pos:
          folded_dots.append(dot)
        else:
          folded_dots.append((fold_pos - (dotx - fold_pos), doty))

  # remove duplicates
  folded_dots = list(set(folded_dots))
  return folded_dots


def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  dots = [tuple(parse("{:d},{:d}", l)) for l in puzzle_input if "fold along" not in l]
  fold_instructions = [tuple(parse("fold along {:l}={:d}", l)) for l in puzzle_input if "fold along" in l]

  # print_dots(dots)
  print()
  print(f"starting length: {len(dots)}")
  dots = fold(dots, fold_instructions[0])
  # print_dots(dots)
  print(f"one fold in: {len(dots)}")

if __name__ == "__main__":
  main()
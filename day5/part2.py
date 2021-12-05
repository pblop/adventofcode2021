import sys
from parse import *

def order(_1, _2):
  return max(_1, _2), min(_1, _2)

class Line:
  def __init__(self, inputline) -> None:
    result = parse("{:d},{:d} -> {:d},{:d}", inputline)
    self.p1 = (result[0], result[1])
    self.p2 = (result[2], result[3])

  def get_extremes(self):
    return (self.p1, self.p2)

  def is_diagonal(self):
    (x1, y1), (x2, y2) = self.get_extremes()
    return x1 != x2 and y1 != y2

  def get_slope(self):
    (x1, y1), (x2, y2) = self.get_extremes()
    return 1 if x1-x2 == y1-y2 else -1

  def get_points_in_line(self):
    points = []

    if self.is_diagonal():
      (x1, y1), (x2, y2) = self.get_extremes()
      (xm, xn) = order(x1, x2)
      slope = self.get_slope()

      # get point whose x is the smallest.
      # also, point whose x is the largest.
      if xn == x1:
        (sm_x, sm_y) = x1, y1
        (la_x, la_y) = x2, y2
      else:
        (sm_x, sm_y) = x2, y2
        (la_x, la_y) = x1, y1

      for i in range(la_x-sm_x+1):
        points.append((sm_x+i, sm_y+i*slope))

    else:
      (x1, y1), (x2, y2) = self.get_extremes()
      (xm, xn), (ym, yn) = order(x1, x2), order(y1, y2)
      for x in range(xn, xm+1):
        for y in range(yn, ym+1):
          points.append((x, y))

    return points

def main():
  puzzle_input = [Line(l.strip()) for l in sys.stdin.readlines() if l.strip() != ""]
  
  #determine map size
  max_x, max_y = 0, 0
  for line in puzzle_input:
    (x1, y1), (x2, y2) = line.get_extremes()
    (xm, _), (ym, _) = order(x1, x2), order(y1, y2)
    if xm > max_x:
      max_x = xm
    if ym > max_y:
      max_y = ym
  
  print(f"max x and y: {max_x}, {max_y}")
  print(f"array size: {max_x+1}, {max_y+1}")
  
  coord_map = [[0]*(max_y+1) for _ in range(max_x+1)]

  # draw map - troubleshooting
  # for y in range(max_y + 1):
  #   for x in range(max_x + 1):
  #     print("." if coord_map[x][y] == 0 else coord_map[x][y], end=" ")
  #   print()
  # print("====")

  for i, line in enumerate(puzzle_input):
    print(f"{i}/{len(puzzle_input)}")
    # print(f"Line: {line.get_extremes()}. {line.is_diagonal()}, {line.get_points_in_line()}")
    for point in line.get_points_in_line():
      x,y = point
      coord_map[x][y] += 1

  # draw map - troubleshooting
  # for y in range(max_y + 1):
  #   for x in range(max_x + 1):
  #     print("." if coord_map[x][y] == 0 else coord_map[x][y], end=" ")
  #   print()
  # print("====")

  num_2overlap = 0
  for x in range(max_x + 1):
    for y in range(max_y + 1):
      if coord_map[x][y] >= 2:
        num_2overlap += 1


  print(num_2overlap)


if __name__ == "__main__":
  main()
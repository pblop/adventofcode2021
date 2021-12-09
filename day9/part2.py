import sys

def find_adjacent_points(heightmap, i, j):
  adjacent_points = []
  if i != 0:
    adjacent_points.append((i-1, j))
  if j != 0:
    adjacent_points.append((i, j-1))
  if i != len(heightmap) - 1:
    adjacent_points.append((i+1, j))
  if j != len(heightmap[0]) - 1:
    adjacent_points.append((i, j+1))
  return adjacent_points

current_basin = []
def find_basin(heightmap, i, j, first_call=True):
  global current_basin
  if first_call:
    current_basin = []

  adjacent_points = find_adjacent_points(heightmap, i, j)
  for ap_i, ap_j in adjacent_points:
    if (ap_i, ap_j) not in current_basin and heightmap[ap_i][ap_j] != 9:
      current_basin.append((ap_i, ap_j))
      find_basin(heightmap, ap_i, ap_j, False)
  
  if first_call:
    return current_basin

def main():
  global current_basin
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  heightmap = [[int(x) for x in list(l)] for l in puzzle_input]
  
  basins = []
  for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
      current_point = heightmap[i][j]
      adjacent_points = find_adjacent_points(heightmap, i, j)

      is_low_point = len([(i, j) for i, j in adjacent_points if heightmap[i][j] <= current_point]) == 0

      if is_low_point:
        basins.append(find_basin(heightmap, i, j))

  basin_lengths = [len(basin) for basin in basins]
  basin_lengths = sorted(basin_lengths)[::-1]
  print(basin_lengths[0] * basin_lengths[1] * basin_lengths[2])

if __name__ == "__main__":
  main()
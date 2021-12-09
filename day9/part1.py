import sys
def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  heightmap = [[int(x) for x in list(l)] for l in puzzle_input]
  
  risk_level_sum = 0
  for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
      adjacent_points = []
      current_point = heightmap[i][j]
      if i != 0:
        adjacent_points.append(heightmap[i-1][j])
      if j != 0:
        adjacent_points.append(heightmap[i][j-1])
      if i != len(heightmap) - 1:
        adjacent_points.append(heightmap[i+1][j])
      if j != len(heightmap[0]) - 1:
        adjacent_points.append(heightmap[i][j+1])
      
      is_low_point = len([ap for ap in adjacent_points if ap <= current_point]) == 0

      if is_low_point:
        risk_level_sum += 1 + current_point

  print(risk_level_sum)
if __name__ == "__main__":
  main()
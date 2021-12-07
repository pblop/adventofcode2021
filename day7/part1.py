import sys

def calculate_fuel(crabs, position):
  fuel = 0
  for crab in crabs:
    fuel += abs(crab - position)
  return fuel

def main():
  crabs = [int(n) for n in sys.stdin.readlines()[0].split(",")]
  max_pos = max(crabs)
  
  min_fuel = calculate_fuel(crabs, 0)
  min_pos = 0
  for pos in range(1, max_pos+1):
    fuel = calculate_fuel(crabs, pos)
    if fuel < min_fuel:
      min_fuel, min_pos = fuel, pos

  print(f"{min_pos}: {min_fuel}")

if __name__ == "__main__":
  main()
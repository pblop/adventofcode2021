import sys

def ppf(fish):
  return ','.join(str(x) for x in fish)

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines()]
  fish = [int(n) for n in puzzle_input[0].split(",")]

  fish_numbers = [0]*9
  for f in fish:
    fish_numbers[f] += 1

  print(f"Initial state: {fish_numbers}")

  for day in range(256):
    fish_numbers = [fish_numbers[1], fish_numbers[2], fish_numbers[3], fish_numbers[4], fish_numbers[5], fish_numbers[6], fish_numbers[0] + fish_numbers[7], fish_numbers[8], fish_numbers[0]] 

    print(day)

  print(sum(fish_numbers))



if __name__ == "__main__":
  main()
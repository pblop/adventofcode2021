import sys

def ppf(fish):
  return ','.join(str(x) for x in fish)

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines()]
  fish = [int(n) for n in puzzle_input[0].split(",")]

  print(f"Initial state: {ppf(fish)}")

  days = 0

  while days != 80:
    days += 1
    for i, f in enumerate(fish.copy()):
      if f == 0:
        fish.append(8)
        fish[i] = 6
      else:
        fish[i] -= 1
    # print(f"After {days} days: {ppf(fish)}")

  print(len(fish))



if __name__ == "__main__":
  main()
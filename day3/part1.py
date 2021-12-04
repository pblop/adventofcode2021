import sys

def main():
  puzzle_input = [l for l in sys.stdin.readlines()]

  # Record bit frequency for all lines
  # freq = [[0, 0]] * len(puzzle_input[0])
  # /\ this creates mirrored lists. \/ this doesn't
  freq = [[0, 0] for _ in range(len(puzzle_input[0])-1)]
  for bn in puzzle_input:
    for i in range(len(bn)-1):
      if bn[i] == '0':
        freq[i][0] += 1
      else: # bn[i] == '1'
        freq[i][1] += 1

  gamma, epsilon = "", ""
  for f in freq:
    if f[0] > f[1]:
      gamma += "0"
      epsilon += "1"
    elif f[1] > f[0]:
      gamma += "1"
      epsilon += "0"
    else:
      print("this shouldn't be reached")

  gamma, epsilon = int(gamma, 2), int(epsilon, 2)
  print(gamma * epsilon)


if __name__ == "__main__":
  main()
import sys

def calculate_most_common(num_list, i):
  zeroes, ones = 0, 0
  for bn in num_list:
    if bn[i] == '0':
      zeroes += 1
    else: # bn[i] == '1'
      ones += 1
  return '1' if ones >= zeroes else '0'

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines()]

  # Record bit frequency for every bit
  # freq = [[0, 0]] * (len(puzzle_input[0]) - 1)
  # /\ this creates mirrored lists. \/ this doesn't

  # Oxygen generator
  oxygen = None
  co2 = None

  nums_oxygen = puzzle_input
  nums_co2 = puzzle_input
  for bit_n in range(len(puzzle_input[0])):
    # Keep numbers with 'most_common[bit_n]' in position 'bit_n'.

    nums_oxygen = [n for n in nums_oxygen if n[bit_n] == calculate_most_common(nums_oxygen, bit_n)]
    nums_co2 = [n for n in nums_co2 if n[bit_n] != calculate_most_common(nums_co2, bit_n)]

    if len(nums_oxygen) == 1:
      oxygen = int(nums_oxygen[0], 2)
    if len(nums_co2) == 1:
      co2 = int(nums_co2[0], 2)
    if len(nums_oxygen) <= 1 and len(nums_co2) <= 1:
      break
    
  print(oxygen * co2)


if __name__ == "__main__":
  main()
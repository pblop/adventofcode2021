import sys

def sort_alphabetically(string: str) -> str:
  return ''.join(sorted(string))

def getnumfromdigits(digit: str) -> int:
  match sort_alphabetically(digit):
    case "abcefg":
      return 0
    case "cf":
      return 1
    case "acdeg":
      return 2
    case "acdfg":
      return 3
    case "bcdf":
      return 4
    case "abdfg":
      return 5
    case "abdefg":
      return 6
    case "acf":
      return 7
    case "abcdefg":
      return 8
    case "abcdfg":
      return 9
    case _:
      return -1

def invert_dict(dictt: dict) -> dict:
  n_dict = {}
  for k, v in dictt.items():
    n_dict[v] = k
  return n_dict

def main() -> None:
  entries = [[x.split(" ") for x in l.strip().split(" | ")] for l in sys.stdin.readlines() if l.strip() != ""]
  
  results = []
  for entry in entries:
    # this map maps every wire in the seven segment display (a-g)
    # to a new wire.
    switch_map = {}
    # this holds (almost) every number and its corresponding digit (numbers changed).
    numbers = {}

    patterns, output = entry
    all_digits = set([sort_alphabetically(d) for d in set(patterns + output)])

    for digit in all_digits:
      match len(digit):
        case 2:
          # digit is a 1.
          # 1s turn on c and f
          numbers[1] = list(digit)
        case 4:
          # digit is a 4.
          # 4s turn on b, c, d, f
          numbers[4] = list(digit)
        case 3:
          # digit is a 7
          # 7s turn on a, c, f
          numbers[7] = list(digit)
        case 7:
          # digit is an 8
          # 8s turn on a, b, c, d, e, f, g
          numbers[8] = list(digit)

    switch_map['a'] = list(set(numbers[7]) - set(numbers[1]))[0]

    # with set(numbers[4])- set(numbers[1]) i get b and d
    # then i check for digits with a length of 5
    # -> if they are missing one of b and d, they must be either a 2 or a 3
    # those two only lack the b, so i know they one they are missing is the b
    # and the one they are not is the d.
    # -> if they have both b and d, that's a 5
    # check which of the wires 1 has they are missing, the one they are missing
    # is c, the other is f.

    bd = list(set(numbers[4]) - set(numbers[1]))
    len5 = [digit for digit in all_digits if len(digit) == 5]
    for digit in len5:
      if bd[0] in digit and bd[1] in digit:
        # d is a 5.
        numbers[5] = digit
        switch_map['c'] = numbers[1][0] if numbers[1][0] not in digit else numbers[1][1]
        switch_map['f'] = numbers[1][1] if numbers[1][0] not in digit else numbers[1][0]
      else:
        # d is a 2 or a 3
        switch_map['b'] = bd[0] if bd[0] not in digit else bd[1]
        switch_map['d'] = bd[1] if bd[0] not in digit else bd[0]

    # now that we know f we can find 2, and 3.
    for digit in len5:
      if digit != numbers[5]:
        if switch_map['f'] in digit:
          # 3.
          numbers[3] = digit
        else:
          # 2.
          numbers[2] = digit
    
    # 2 and 3 share every letter but e and f.
    # if we remove every letter in 3 from 2, we will get e.
    switch_map['e'] = list(set(numbers[2]) - set(numbers[3]))[0]

    # g is the remaining letter
    switch_map['g'] = list(set("abcdefg") - set(switch_map.values()))[0]

    # we did it! yay!
    # now we decode!
    inverse_switch_map = invert_dict(switch_map)

    result = ""
    for digit in output:
      untangled_digit = ''.join([inverse_switch_map[letter] for letter in digit])
      result += str(getnumfromdigits(untangled_digit))

    results.append(int(result))

  print(sum(results))
  
if __name__ == "__main__":
  main()
import sys
from typing import Dict, List

def step(polymer_template, polymer_rules):
  i = 0
  polymer_template_len = len(polymer_template)
  while i < polymer_template_len:
    if i < polymer_template_len - 1:
      letter, next_letter = polymer_template[i], polymer_template[i+1]
      pair = letter + next_letter
      insert_letter = polymer_rules[pair]
      # print(f"{letter}, {next_letter} => {pair} => {insert_letter}")
      
      polymer_template.insert(i+1, insert_letter)
      i += 1
      polymer_template_len += 1

    i += 1
  
  return polymer_template

def occurrences(string: str) -> Dict[str, int]:
  occurrence_dict = {}
  for ch in string:
    if ch not in occurrence_dict:
      occurrence_dict[ch] = 0

    occurrence_dict[ch] += 1

  return occurrence_dict


def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  polymer_template = list(puzzle_input[0])
  polymer_rules = {rl.split(" -> ")[0]: rl.split(" -> ")[1] for rl in puzzle_input[1:]}

  print(f"Template: {''.join(polymer_template)}")
  print(f"Rules: {polymer_rules}")

  for i in range(1, 11):
    polymer_template = step(polymer_template, polymer_rules)
    # print(f"After step {i}: {''.join(polymer_template)}")
    print(f"After step {i}: len={len(polymer_template)}")
    o = occurrences(polymer_template)
    frequency_list = sorted(o.values())

    print(f"    {frequency_list[-1]} - {frequency_list[0]} = {frequency_list[-1] - frequency_list[0]}")

if __name__ == "__main__":
  main()
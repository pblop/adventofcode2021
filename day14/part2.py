import sys
from typing import Dict, List

# TODO: Second part. If I use the first part's algorithm, it's too slow and
# it won't ever reach the last required iteration.

# POSSIBLE SOLUTIONS:
# 1. Cache 5 or 10 pair sequences and have a lookup table, going through
# the input 5-10 pairs at once, copying the resulting output onto another string (output).
#    Problem: I'd also need to check the pairs made by the last element of a
#    pair sequence and the first element of the next one, and add the corresponding
#    polymer.
#    Pros: This should be possible to make programmatically, and store longer sequences at
#    the same time they are being calculated.
def step(polymer_template, polymer_rules):
  # i = 0
  # polymer_template_len = len(polymer_template)
  # while i < polymer_template_len:
  #   if i < polymer_template_len - 1:
  #     insert_letter = polymer_rules[polymer_template[i] + polymer_template[i+1]]
      
  #     i += 1
  #     polymer_template.insert(i, insert_letter)
  #     polymer_template_len += 1
      
  #   i += 1
  
  # return polymer_template

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

  for i in range(1, 41):
    polymer_template = step(polymer_template, polymer_rules)
    # print(f"After step {i}: {''.join(polymer_template)}")
    print(f"After step {i}: len={len(polymer_template)}")
    o = occurrences(polymer_template)
    frequency_list = sorted(o.values())

    print(f"    {frequency_list[-1]} - {frequency_list[0]} = {frequency_list[-1] - frequency_list[0]}")

if __name__ == "__main__":
  main()
import sys

ERROR_SCORE_TABLE = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
AUTOCOMPLETE_SCORE_TABLE = { ")": 1, "]": 2, "}": 3, ">": 4 }
BRACKET_MATCH_TABLE = { "(": ")", "[": "]", "{": "}", "<": ">" }
# BRACKET_MATCH_TABLE = { ")": "(", "]": "[", "}": "{", ">": "<" }


def check_and_fix_line(line: str):
  opening_chars = []
  for ch in line:
    if ch in ["[", "(", "{", "<"]:
      opening_chars.append(ch)
    else: # ch in ["]", ")", "}", ">"]
      if BRACKET_MATCH_TABLE[opening_chars[-1]] == ch:
        opening_chars.pop()
      else:
        return BRACKET_MATCH_TABLE[opening_chars[-1]], ch
  
  autocomplete_string = ""
  for ch in opening_chars[::-1]:
    autocomplete_string += BRACKET_MATCH_TABLE[ch]

  return autocomplete_string

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines()]

  autocomplete_scores = []
  for i, line in enumerate(puzzle_input):
    result = check_and_fix_line(line)

    
    if isinstance(result, str):
      # correct or incomplete line
      if result != "":
        # incomplete line
        autocomplete_score = 0
        for ch in result:
          autocomplete_score = autocomplete_score*5 + AUTOCOMPLETE_SCORE_TABLE[ch]
        autocomplete_scores.append(autocomplete_score)
        print(f"Line {i}: Complete by adding {result}. Autocomplete score: {autocomplete_score}")
      else:
        print(f"Line {i}: OK")
    else:
      # corrupted line
      expected, found = result
      error_score = ERROR_SCORE_TABLE[found]
      print(f"Line {i}: Expected {expected} but found {found} instead. Syntax error score: {error_score}")

      
  autocomplete_scores = sorted(autocomplete_scores)
  print(f"Total autocomplete score: {autocomplete_scores[int(len(autocomplete_scores)/2)]}")

if __name__ == "__main__":
  main()
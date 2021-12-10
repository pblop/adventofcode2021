import sys

SCORE_TABLE = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
BRACKET_MATCH_TABLE = { "(": ")", "[": "]", "{": "}", "<": ">" }
# BRACKET_MATCH_TABLE = { ")": "(", "]": "[", "}": "{", ">": "<" }


def check_line(line: str):
  opening_chars = []
  for ch in line:
    if ch in ["[", "(", "{", "<"]:
      opening_chars.append(ch)
    else: # ch in ["]", ")", "}", ">"]
      if BRACKET_MATCH_TABLE[opening_chars[-1]] == ch:
        opening_chars.pop()
      else:
        return BRACKET_MATCH_TABLE[opening_chars[-1]], ch
  return None

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines()]

  total_syntax_error_score = 0
  for i, line in enumerate(puzzle_input):
    check_result = check_line(line)

    # Corrupted lines
    if check_result != None:
      expected, found = check_result
      error_score = SCORE_TABLE[found]
      total_syntax_error_score += error_score
      print(f"Line {i}: Expected {expected} but found {found} instead. Syntax error score: {error_score}")

  print(f"Total syntax error score: {total_syntax_error_score}")

if __name__ == "__main__":
  main()
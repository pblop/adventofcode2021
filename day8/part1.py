import sys
def main():
  entries = [[x.split(" ") for x in l.strip().split(" | ")] for l in sys.stdin.readlines() if l.strip() != ""]
  
  instances_unique_digits = 0
  for entry in entries:
    patterns, output = entry

    for digit in output:
      if len(digit) in [2, 4, 3, 7]:
        instances_unique_digits += 1

    # print(f"patterns: {patterns}")
    # print(f"output: {output}")
  
  print(instances_unique_digits)

if __name__ == "__main__":
  main()
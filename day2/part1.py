import sys

def parse_instruction(ins):
  ins = ins.split(" ")
  return (ins[0], int(ins[1]))

def main():
  instructions = [parse_instruction(l) for l in sys.stdin.readlines()]

  x, y = 0, 0
  for ins in instructions:
    match (ins):
      case ("forward", _):
        x += ins[1]
      case ("down", _):
        y += ins[1]
      case ("up", _):
        y -= ins[1]
  
  print(x*y)


if __name__ == "__main__":
  main()
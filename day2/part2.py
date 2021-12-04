import sys

def parse_instruction(ins):
  ins = ins.split(" ")
  return (ins[0], int(ins[1]))

def main():
  instructions = [parse_instruction(l) for l in sys.stdin.readlines()]

  x, y, aim = 0, 0, 0
  for ins in instructions:
    match (ins):
      case ("forward", _):
        x += ins[1]
        y += aim * ins[1]
      case ("down", _):
        aim += ins[1]
      case ("up", _):
        aim -= ins[1]
  
  print(x*y)


if __name__ == "__main__":
  main()
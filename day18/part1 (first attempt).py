import sys
import ast


# sfn -> snailfish number

class Pair():
  '''
  A Pair consists of two elements: [e1, e2]
  They can be either a Pair or an int.
  '''
  def __init__(self, array) -> None:
    self.array = array

  def __str__(self) -> str:
    return f"p:{self.array}"

  def __repr__(self) -> str:
    return self.__str__()

def isreduced(sfn):
  pass

def explode(pair):
  pass

def reduce(pair):
  # traverse pairs
  current_pos = []
  pair_parent = None
  depth = 0
  while True:
    if depth == 4:
      pass
    
    if isinstance(pair_parent[0], Pair):

      current_pos.append(0)

    depth += 1


def parsepair(pair):
  parsed_pair_array = [None, None]

  if isinstance(pair[0], int):
    parsed_pair_array[0] = pair[0]
  else:
    parsed_pair_array[0] = parsepair(pair[0])

  if isinstance(pair[1], int):
    parsed_pair_array[1] = pair[1]
  else:
    parsed_pair_array[1] = parsepair(pair[1])

  return Pair(parsed_pair_array)

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  sfns = [ast.literal_eval(l) for l in puzzle_input]

  # for sfn in sfns:
  #   print(sfn)

  # [[[[[9,8],1],2],3],4]
  sfn = [[[[[9,8],1],2],3],4]
  print(sfn)
  parsed = parsepair(sfn)
  print(parsed)
  reduce(parsed)
  print(parsed)
    



if __name__ == "__main__":
  main()

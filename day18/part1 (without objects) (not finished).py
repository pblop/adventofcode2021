import sys
import ast
from anytree import Node, RenderTree, PreOrderIter, LevelOrderGroupIter
from math import ceil, floor

# sfn -> snailfish number
# rn -> regular number

def willexplode(tree):
  return any(node.depth > 4 for node in PreOrderIter(tree))

def explode(tree):
  # explode
  # rn -> regular number
  last_left_rn = None
  elem_to_explode = None
  first_right_rn = None
  for node in PreOrderIter(tree):
    # print(f"Nested inside 4 pairs: {node.depth > 4}")
    if elem_to_explode == None:
      if node.depth > 4:
        # the leftmost pair nested inside 4 pairs.
        # print("Pair must explode")
        elem_to_explode = node.parent
      elif hasattr(node, "value"):
        last_left_rn = node
    else:
      if node.parent != elem_to_explode and hasattr(node, "value"):
        first_right_rn = node
        break
  # print(f"left {last_left_rn}")
  # print(f"right {first_right_rn}")
  # print(RenderTree(elem_to_explode))

  if last_left_rn != None:
    last_left_rn.value += elem_to_explode.children[0].value
  if first_right_rn != None:
    first_right_rn.value += elem_to_explode.children[1].value

  elem_to_explode.children = []
  elem_to_explode.value = 0

def willsplit(tree):
  return any(node.value >= 10 for node in PreOrderIter(tree) if hasattr(node, "value"))

def split(tree):
  # explode
  # rn -> regular number
  for node in PreOrderIter(tree):
    if hasattr(node, "value") and node.value >= 10:
      Node("0", parent=node, value=floor(node.value/2))
      Node("1", parent=node, value=ceil(node.value/2))
      del node.value
      break    

def reduce(tree):
  # traverse pairs
  while willexplode(tree) or willsplit(tree):
    while willexplode(tree):
      print("exploding")
      explode(tree)
    while willsplit(tree):
      print("splitting")
      split(tree)

def parsepair(pair, parent):
  if isinstance(pair[0], int):
    Node(0, parent=parent, value=pair[0])
  else:
    p = Node(0, parent=parent)
    parsepair(pair[0], p)

  if isinstance(pair[1], int):
    Node(1, parent=parent, value=pair[1])
  else:
    p = Node(1, parent=parent)
    parsepair(pair[1], p)

def intopair(root):
  pair = []

  for child in root.children:
    if hasattr(child, "value"):
      pair.append(child.value)
    else:
      pair.append(intopair(child))

  return pair
def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  sfns = [ast.literal_eval(l) for l in puzzle_input]

  # for sfn in sfns:
  #   print(sfn)

  # exploding tests
  # sfn = [[[[[9,8],1],2],3],4]
  # sfn = [7,[6,[5,[4,[3,2]]]]]
  # sfn = [[6,[5,[4,[3,2]]]],1]
  # sfn = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

  # exploding + splitting test
  sfn=[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
  print(sfn)
  root = Node("root")
  parsepair(sfn, root)
  print(intopair(root))
  print(RenderTree(root))
  reduce(root)
  print(RenderTree(root))
  print(intopair(root))
    



if __name__ == "__main__":
  main()
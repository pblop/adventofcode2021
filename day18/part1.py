from __future__ import annotations
import sys
import ast
from anytree import Node, RenderTree, PreOrderIter, findall
from math import ceil, floor

# sfn -> snailfish number
# rn -> regular number

def willexplode(tree):
  return any(node.depth > 4 for node in PreOrderIter(tree))
def willsplit(tree):
  return any(node.value >= 10 for node in PreOrderIter(tree) if hasattr(node, "value"))
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
def getmagnitude(root_orig):
  root = clone(root_orig)
  while True:
    pairstoreduce = [node for node in PreOrderIter(root) if len(node.children) == 2 and all(hasattr(child, "value") for child in node.children)]
    if len(pairstoreduce) == 0:
      break

    for pairnode in pairstoreduce:
      magnitude = 3*pairnode.children[0].value + 2*pairnode.children[1].value
      pairnode.children = []
      pairnode.value = magnitude
  return root.value
def clone(tree):
  # I'm too lazy to make a clone function
  # so I'm just serialising and deserialising the
  # tree
  new_tree = Node("root")
  parsepair(intopair(tree), new_tree)

  return new_tree


class SnailfishNumber():
  def __init__(self, sfn_as_pair) -> None:
    self.tree = Node("root")
    parsepair(sfn_as_pair, self.tree)

  def explode(self):
    # explode
    # rn -> regular number
    last_left_rn = None
    elem_to_explode = None
    first_right_rn = None

    max_depth = max(node.depth for node in PreOrderIter(self.tree))

    for node in PreOrderIter(self.tree):
      if elem_to_explode == None:
        if node.depth == max_depth:
          # the leftmost pair nested inside 4 pairs.
          elem_to_explode = node.parent
        elif hasattr(node, "value"):
          last_left_rn = node
      else:
        if node.parent != elem_to_explode and hasattr(node, "value"):
          first_right_rn = node
          break
    
    if last_left_rn != None:
      last_left_rn.value += elem_to_explode.children[0].value
    if first_right_rn != None:
      first_right_rn.value += elem_to_explode.children[1].value

    elem_to_explode.children = []
    elem_to_explode.value = 0

  def split(self):
    # explode
    # rn -> regular number
    for node in PreOrderIter(self.tree):
      if hasattr(node, "value") and node.value >= 10:
        Node("0", parent=node, value=floor(node.value/2))
        Node("1", parent=node, value=ceil(node.value/2))
        del node.value
        break    

  def reduce(self):
    # traverse pairs
    while willexplode(self.tree) or willsplit(self.tree):
      while willexplode(self.tree):
        print("exploding")
        self.explode()
      if willsplit(self.tree):
        print("splitting")
        self.split()

  def as_pair(self):
    return intopair(self.tree)

  def magnitude(self):
    return getmagnitude(self.tree)

  def __add__(self, other: SnailfishNumber) -> SnailfishNumber:
    added_sfn = SnailfishNumber([self.as_pair(), other.as_pair()])
    added_sfn.reduce()

    return added_sfn

  def __str__(self) -> str:
    return str(self.as_pair())
  def __repr__(self) -> str:
    return self.__str__()

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines() if l.strip() != ""]
  sfns = [ast.literal_eval(l) for l in puzzle_input]

  sum_sfns = SnailfishNumber(sfns[0])
  for sfn in sfns[1:]:
    # print(f"sum so far: {sum_sfns}")
    # print(f"new: {sfn}")
    sum_sfns = sum_sfns + SnailfishNumber(sfn)
    # print(f"result: {sum_sfns}")
  print(sum_sfns)
  print(sum_sfns.magnitude())
  # exploding tests
  # sfn = [[[[[9,8],1],2],3],4]
  # sfn = [7,[6,[5,[4,[3,2]]]]]
  # sfn = [[6,[5,[4,[3,2]]]],1]
  # sfn = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]

  # exploding + splitting test
  # sfn1 = SnailfishNumber([[[[4,3],4],4],[7,[[8,4],9]]])
  # sfn2 = SnailfishNumber([1,1])
  # sfn = sfn1+sfn2
  # print(sfn.magnitude())
  # print(SnailfishNumber([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]).magnitude())
    



if __name__ == "__main__":
  main()
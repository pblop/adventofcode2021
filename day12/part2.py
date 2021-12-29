import sys
from typing import List, Tuple

# This passes the first part of the 12th day of AOC 2021.
# It also passes the example that's given, with the exact same result,
# but not the two examples to which the correct output is given.
# It also doesn't pass the challenge input (understandable given I can't
# get it to pass two of the three examples I've been given).
# I don't know what's wrong and don't have energy to keep debugging it
# (I don't even have an incorrect answer to backtrace the error) or 
# completely remaking it.

# I've made this 'when2log' function that allows me to log based on certain
# conditions.
when2log = lambda history: len(history) == 5 and history[1] == "A" and history[2] == "b" and history[3] == "A" #["start", "A", "b", "A", "c", "A"]:

class Path:
  def __init__(self, current: str  = "start", history: List[str] = []) -> None:
    self.current = current
    self.history = history
  
  def finished(self):
    return self.current == "end"
  
  def has_visited(self, loc: str):
    return loc in self.history

  def visited_count(self, loc: str):
    return self.history.count(loc)

  def can_visit_lower(self, loc: str):
    # if len(self.history) == 4 and self.history[1] == "A" and self.history[2] == "b" and self.history[3] == "A": #["start", "A", "b", "A", "c", "A"]:
    #   print(self.aoc_format())
    #   print(loc)
    #   print([l for l in self.history if self.history.count(l) == 2])
    has_visited_lower_twice = len([l for l in self.history if l != "start" and l.islower() and self.history.count(l) == 2]) != 0
    
    # if when2log(self.history):
    #   print("canvisitlower")
    #   print(self.aoc_format())
    #   print("  hvl2", has_visited_lower_twice)
    #   print("  hist", self.history)
    #   print("  lowr", [l for l in self.history if l.lower()])
    #   print("  hist", self.history)

    if has_visited_lower_twice:
      return not self.has_visited(loc)
    else:
      return self.visited_count(loc) < 2

  def aoc_format(self):
    return ",".join(self.history + [self.current])
  
  def __repr__(self) -> str:
    return f"Path(current={self.current}, history={self.history})"

class ConnectionMap:
  def __init__(self, connections: List[Tuple[str, str]]) -> None:
    self.connections = connections
  
  def getconnections(self, current_location: str) -> List[str]:
    possible_connections = []
    for l1, l2 in self.connections:
      if current_location == l1:
        possible_connections.append(l2)
      elif current_location == l2:
        possible_connections.append(l1)
    return possible_connections

  def walk(self, paths: List[Path] = [Path()]) -> List[Path]:
    unfinished_paths = [p for p in paths if not p.finished()]
    # return when we have visited every path
    if len(unfinished_paths) == 0:
      return paths

    for path in unfinished_paths:
      # remove the current path from the list of paths we pass to the next iteration
      # because we've already handled it, and don't want that function to handle it
      # again.
      paths.remove(path)

      possible_next_locs = self.getconnections(current_location=path.current)
      # if when2log(path.history):
      #   print("m")
      #   print(path.aoc_format())
      #   print(1, possible_next_locs)

      # check every location in the possible next locations
      # rule out illegal ones (we can visit one small cave twice, and the rest once)
      # for every legal location, we add a new path.

      # uppercase cave is always legal
      # lowercase cave is only legal if we haven't visited it yet (we can only visit one twice and the rest once)
      possible_next_locs = [l for l in possible_next_locs if l != "start" and (l.isupper() or (l.islower() and path.can_visit_lower(l)))]
      # if when2log(path.history):
      #   print(2, possible_next_locs)
      #   print("\n")

      for location in possible_next_locs:
        new_path = Path(
            current=location, 
            history=(path.history + [path.current])
            )
        paths.append(new_path)
    
    return self.walk(paths)

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines()]
  connections = [l.split("-") for l in puzzle_input]
  m = ConnectionMap(connections)
  print("\n".join([p.aoc_format() for p in m.walk()]))
  print(len(m.walk()))


if __name__ == "__main__":
  main()
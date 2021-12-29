import sys
from typing import List, Tuple

class Path:
  def __init__(self, current: str  = "start", history: List[str] = []) -> None:
    self.current = current
    self.history = history
  
  def finished(self):
    return self.current == "end"
  
  def has_visited(self, loc: str):
    return loc in self.history
  
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
      # check every location in the possible next locations
      # rule out illegal ones (we can only visit small caves once)
      # for every legal location, we add a new path.

      # uppercase cave is always legal
      # lowercase cave is only legal if we haven't visited it yet (we can only visit it once)
      possible_next_locs = [l for l in possible_next_locs if l.isupper() or (l.islower() and not path.has_visited(l))]
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
  print(len(m.walk()))


if __name__ == "__main__":
  main()
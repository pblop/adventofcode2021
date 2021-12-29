import sys

class Octopus:
  def __init__(self, el) -> None:
    self.energy_level = el
    self.has_flashed = False

  def increase(self):
    if not self.has_flashed:
      self.energy_level += 1

  def flash_if_necessary(self):
    if self.energy_level > 9:
      self.energy_level = 0
      self.has_flashed = True
      return True
    return False

  def new_step(self):
    self.has_flashed = False

def any_octopus_that_should_flash(octopuses): 
  for row in octopuses:
    for op in row:
      if op.energy_level > 9 and not op.has_flashed:
        return True
  
  return False

def all_octopuses_have_flashed(octopuses):
  # Check if all octopuses have flashed.
  for row in octopuses:
    for op in row:
      if op.energy_level != 0:
        return False

  return True

def print_octopuses(octopuses):
  for row in octopuses:
    for op in row:
      print(str(op.energy_level).rjust(3), end="")
    print()
  print()

def main():
  puzzle_input = [l.strip() for l in sys.stdin.readlines()]
  octopuses = [[Octopus(int(x)) for x in list(l)] for l in puzzle_input]

  print("Before any steps:")
  print_octopuses(octopuses)

  step_n = 0
  flashes = 0
  while True:
    # the energy level of each octopus increases by 1.
    for row in octopuses:
      for op in row:
        op.new_step()
        op.increase()

    while any_octopus_that_should_flash(octopuses):
      for i, row in enumerate(octopuses):
        for j, op in enumerate(row):
          # print_octopuses(octopuses)
          if not op.has_flashed and op.flash_if_necessary():
            # this octopus has flashed for the first time this step
            flashes += 1
            if i > 0:
              octopuses[i-1][j].increase()
            if j > 0:
              octopuses[i][j-1].increase()
            if i < len(octopuses) - 1:
              octopuses[i+1][j].increase()
            if j < len(octopuses[0]) - 1:
              octopuses[i][j+1].increase()
            # diagonals
            if i > 0 and j > 0:
              octopuses[i-1][j-1].increase()
            if i < len(octopuses) - 1 and j < len(octopuses[0]) - 1:
              octopuses[i+1][j+1].increase()
            if i > 0 and j < len(octopuses[0]) - 1:
              octopuses[i-1][j+1].increase()
            if i < len(octopuses) - 1 and j > 0:
              octopuses[i+1][j-1].increase()

    print(f"After step {step_n+1}:")
    print_octopuses(octopuses)
    
    if step_n == 99:
      break

    step_n += 1
  print(flashes)

if __name__ == "__main__":
  main()
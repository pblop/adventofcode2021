from parse import *
import itertools as it

# returns whether the probe will reach the target or not
def willreachtarget(probe_velocity, target):
  x, y = 0, 0
  v_x, v_y = probe_velocity
  x_min, x_max, y_min, y_max = target

  max_reached_y = y

  i = 0
  while True:
    # print(f"#{i}: x={x}, y={y}")
    i += 1
    # The probe's x position increases by its x velocity.
    # The probe's y position increases by its y velocity.
    x += v_x
    y += v_y

    # Due to drag, the probe's x velocity changes by 1 toward the value 0; 
    # that is, it decreases by 1 if it is greater than 0, increases by 1 if 
    # it is less than 0, or does not change if it is already 0.
    if v_x < 0:
      v_x += 1
    elif v_x > 0:
      v_x -= 1
    
    # Due to gravity, the probe's y velocity decreases by 1.
    v_y -= 1

    if y > max_reached_y:
      max_reached_y = y

    if x_min <= x <= x_max and y_min <= y <= y_max:
      return True, max_reached_y, x, y
    
    # If we've reached this statement and our y is lower than the minimum value,
    # we can be certain we will not reach the target position.
    if y < y_min:
      return False, max_reached_y, x, y
    


def main():
  target = tuple(parse("target area: x={:d}..{:d}, y={:d}..{:d}", input()))

  x_min, x_max, y_min, y_max = target
  print(f"x_min={x_min}, x_max={x_max}, y_min={y_min}, y_max={y_max}")
  # # These statements are for testing if the willreachtarget function works
  # # correctly.
  # print(willreachtarget((7,2), target))
  # print(willreachtarget((6,3), target))
  # print(willreachtarget((9,0), target))
  # print(willreachtarget((17,-4), target))
  # print(willreachtarget((6,9), target))


  # v_x = 0
  # v_y = 0

  # best_velocity = (0, 0, 0) # => (v_x, v_y, max_reached_y)
  # while True:
  #   while True:
  #     reaches_target, max_reached_y = willreachtarget((v_x, v_y), target)
  #     print(f"v_x={v_x}, v_y={v_y}, reaches={reaches_target}, mry={max_reached_y}-{best_velocity[2]}")
  #     if reaches_target and max_reached_y > best_velocity[2]:
  #       best_velocity = v_x, v_y, max_reached_y
  #     elif max_reached_y < best_velocity[2]:
  #       break
  #     v_y += 1
  #   print(best_velocity)

  # (v_x, v_y, max_reached_y)
  best_velocity = (0, 0, 0)
  v_x = 0
  while v_x <= x_max:
    v_y = 0

    while v_y < abs(y_min):
      reaches_target, max_reached_y, x_final, y_final = willreachtarget((v_x, v_y), target)
      print(f"{'✅' if reaches_target else '❌'} v=({v_x}, {v_y}), pos=({x_final}, {y_final}), max_reached_y={max_reached_y}")
      if reaches_target:
        if max_reached_y > best_velocity[2]:
          best_velocity = v_x, v_y, max_reached_y
      else:
        # NOTE: After finishing part 2. I know this way of finding out if
        # the probe x ever reachs x_min is flawed. If y reaches y_min faster
        # than x reaches x_min in the willreachtarget simulation, this 
        # will be true, even if given more steps, x could reach x_min.
        # See part2 for a better way to do this (using a function called
        # willreachx that only simulates x).

        if x_final < x_min:
          print("Didn't reach x_min, increasing v_x by 1")
          v_x += 1
          v_y -= 1 # redo this for loop iteration

      v_y += 1
    v_x += 1
    
  print(f"v_x={best_velocity[0]}, v_y={best_velocity[1]}, max_reached_y={best_velocity[2]}")

  


if __name__ == "__main__":
  main()
from parse import *
import itertools as it

def willreachx(v_x, target):
  x = 0
  x_min, _, _, _ = target

  while True:
    x += v_x
    if v_x < 0:
      v_x += 1
    elif v_x > 0:
      v_x -= 1

    if x >= x_min:
      return True
    
    if v_x == 0:
      return False


# returns whether the probe will reach the target or not
def willreachtarget(probe_velocity, target):
  x, y = 0, 0
  v_x, v_y = probe_velocity
  x_min, x_max, y_min, y_max = target

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

    if x_min <= x <= x_max and y_min <= y <= y_max:
      return True, x, y
    
    # If we've reached this statement and our y is lower than the minimum value,
    # we can be certain we will not reach the target position.
    if y < y_min:
      return False, x, y
    


def main():
  target = tuple(parse("target area: x={:d}..{:d}, y={:d}..{:d}", input()))

  x_min, x_max, y_min, y_max = target
  print(f"x_min={x_min}, x_max={x_max}, y_min={y_min}, y_max={y_max}")

  possible_velocities = []

  # (v_x, v_y, max_reached_y)
  v_x = 0
  while v_x <= x_max:
    v_y = -(abs(y_min))

    if not willreachx(v_x, target):
      v_x += 1
      continue

    while v_y < abs(y_min):
      reaches_target, x_final, y_final = willreachtarget((v_x, v_y), target)
      print(f"{'✅' if reaches_target else '❌'} v=({v_x}, {v_y}), pos=({x_final}, {y_final})")
      if reaches_target:
        possible_velocities.append((v_x, v_y))

      v_y += 1
    v_x += 1
    
  print(len(possible_velocities))

  
if __name__ == "__main__":
  main()
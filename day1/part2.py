import sys

def main():
  measurements = [int(m.strip()) for m in sys.stdin.readlines()]
  
  sliding_windows = [sum(measurements[i:i+3]) for i in range(len(measurements))]

  prev = None
  increases = 0
  for w in sliding_windows:
    if prev != None:
      if w > prev:
        increases += 1
    prev = w

  print(f"{increases}")



if __name__ == "__main__":
  main()
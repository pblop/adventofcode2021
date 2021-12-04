import sys

def main():
  measurements = [int(m.strip()) for m in sys.stdin.readlines()]
  
  prev = None
  increases = 0
  for m in measurements:
    if prev != None:
      if m > prev:
        increases += 1
    prev = m

  print(f"{increases}")



if __name__ == "__main__":
  main()
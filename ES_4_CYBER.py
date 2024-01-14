def f(x):
  if x < 0:
    x -= 2*x
    return f(x)
  if x < 99:
    return x
  x -= 99
  return f(x)

def main():
    ris = f(-12037)
    print(ris)

if __name__ == "__main__":
    main()

def encrypt(l):
  for i in range(0, 3):
    for j in range(i, 3):
      tmp = l[4*i + j]
      l[4*i + j] = l[4*j + i]
      l[4*j + i] = tmp
  return l

def main():
    l = []
    for c in "crocetteolicyber":
        l += c
    ris = encrypt(l)
    print(ris)

if __name__ == "__main__":
    main()
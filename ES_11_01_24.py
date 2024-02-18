def main():
    n = int(input("inserisci un numero dispari: "))
    while ((n % 2) == 0):
        n = int(input("DISPARI! reinserisci un numero: "))
    for k in range(1, n + 1, 2):
        print(" "* ((n-1)//2 - (k//2)) + "*"*k)
    for k in range(1, n, 2):
        print(" "*(k//2+1) + "*"*(n-k-1))
if __name__ == "__main__":
    main()
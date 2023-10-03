def main():
    x = float(input("inserisci il primo numero:"))
    y = float(input("inserisci il secondo numero:"))
    if x>y:
        y, x = x, y #algoritmo di scambio (non servono variabili temporanee)
        #assegnamento multiplo:   int a, b = 5, 7 (int a = 5; int b = 7)
    print(f"{y}, {x}")
if __name__ == "__main__":
    main()
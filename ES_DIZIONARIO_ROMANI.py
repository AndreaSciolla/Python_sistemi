def main():

    valoriRomani = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    romano = input("inserisci un numero romano: ")
    listaRomani = []
    for i in romano:
        listaRomani += i
    listaArabi = []
    for x in listaRomani:
        for chiave in valoriRomani:
            if chiave == x:
                listaArabi.append(valoriRomani[chiave])
    print(listaArabi)

if __name__ == "__main__":
    main()
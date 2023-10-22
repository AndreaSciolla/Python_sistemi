def main():
    lista = []
    k = 0

    while True:
        voto = int(input("inserisci un voto (-1 per interrompere): "))
        if (voto < 0 and k >= 6):
            break
        lista.append(voto)   
        k += 1
    print(f"lista esclusi primo e ultimo: {lista[1:-1]}")
    lista[3] = 10
    print(lista)
if __name__ == "__main__":
    main()
    
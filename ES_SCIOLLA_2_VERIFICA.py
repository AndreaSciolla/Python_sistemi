def main():   
    lista_narcisi = []
    for i in range(1, 999): #era da 1 a 1000
        lista_c = [int(c)**3 for c in str(i)] #list comprehension che carica una lista i cubi di ciascuna cifra del numero
        if sum(lista_c) == i:  #se somma è uguale al numero stesso è narcisista
            lista_narcisi.append(i)
    print(lista_narcisi)
if __name__ == "__main__":
    main()
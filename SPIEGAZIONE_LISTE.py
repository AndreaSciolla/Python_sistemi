#LISTE
#le gli elementi delle liste non perforza sono adiacenti in memoria

def print_list(l):
    print("la lista è:", end=" ")
    for elemento in l:
        print(elemento, end=" ") #end è un parametro che si puo passare alla funzione print si puo cambiare l'ultimo carattere da \n a " "
    print("\n")


def main():
    # l = [1, 2, 3, 4] #esempio di una lista
    #l = [1, 2, 3, "c", 3.14, "python"] #lista con tipi diversi
    #r = [10, 11, 12]
    #print_list(l+r)#concatena le liste
    #print_list(3*r)#concatena la lista r per 3 volte
    #print_list(l[::-1])

    #come caricare una lista
    lista = []
    num = 1
    while num>0:
        num = int(input("scrivi un numero: (-1 per interrompere): "))
        if num>0:
            lista.append(num) #append è un METODO che permette di aggiungere qualcosa alla lista
    print_list(lista)

if __name__ =="__main__":
    main()
#ESERCIZI SUI FOR

def main():
    #i vettori in python si chiamano lista
    lista = [4, 100, 3, "ciao", print] #lista (sequenza di oggetti(anche funzioni))

    """#ciclo for C-style -> non dobbiamo usarlo
    for i in range(0, len(lista)):
        print(f"l'elemnto {i}-esimo della lista è: {lista[i]}")"""

    #ciclo for in Python-style

    for elemento in lista:   #per ogni 'elemento' in lista stampa 'elemento'
        print(f"elemento: {elemento}")

if __name__ == "__main__":
    main()
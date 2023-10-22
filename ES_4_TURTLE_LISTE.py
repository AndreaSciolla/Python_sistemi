#chiedere a utente una lista di comandi da dare 
#forward 100 -> F
#right 90° -> R
#left 90° -> L

import turtle

def print_list(l):
    print("la lista è:", end=" ")
    for elemento in l:
        print(elemento, end=" ") #end è un parametro che si puo passare alla funzione print si puo cambiare l'ultimo carattere da \n a " "
    print("\n")

def disegna(lista, alice):
    for com in lista:
        if com == "f":
            alice.forward(100)
        if com == "r":
            alice.right(90)
        if com == "l":
            alice.left(90)
    
def main():

    lista = []
    comandiPossibili = ["f", "r", "l"] #lista dei comandi possibili
    com = "f"
    while com in comandiPossibili:
        com = (input("scrivi un comando: (n per interrompere): "))
        if com != "n":
            lista.append(com) #append è un METODO che permette di aggiungere qualcosa alla lista
    
    print_list(lista)

    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.shape("turtle")
    alice.color('red', 'blue')#cambia il colore della linea
    
    disegna(lista, alice)

    finestra.mainloop()
if __name__ == "__main__":
    main()
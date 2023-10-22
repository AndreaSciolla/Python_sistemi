#LIST COMPREHENSION -> modo per riempire liste in maniera semplice

#lista con i primi 5 quadrati perfetti
import random


quadrati = [i*i for i in range(1, 6)] #la variabile i viene elevata a 2 e ogni volta viene incrementata
numeri_interi = [i for i in range(1, 11)] #mette i numeri intere da 1 a 11 escluso

stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = [parola for parola in stringhe if parola[0] == "c"] #prende solo le parole che iniziano per 0
#print(quadrati)
#print(numeri_interi)
#print(stringhe)
#print(stringhe_c)

voti = [random.randint(2, 10) for _ in range(10)] #crea una lista di numeri casuali  -> su può usare il _ se non ci serve la variabile
print(voti)
voti_insuff = [voto for voto in voti if(voto < 6)]
print(voti_insuff)
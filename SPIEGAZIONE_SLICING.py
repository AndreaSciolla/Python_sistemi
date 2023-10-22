#SLICING DI STRINGHE
s = "ciao come stai?"  #in python si puo indicizzare in modo alternativo (0, 1, 2, 3 o -4, -3, -2, -1) l'ultimo carattere ha indice -1, auelli prima vengono decrementati di 1
print(f"il primo carattere e': {s[0]}")
print(f"l'ultimo carattere e': {s[-1]}")
print(f"l'ultimo carattere e': {s[len(s)-1]}") #C -style -> non usare
print(f"il penultimo carattere e': {s[-2]}")

print(s[3:7]) #dal carattere 3 al 7 escluso
print(f"tutta la stringa esclusi il primo e ultimo carattere: {s[1:-1]}") #tutta la stringa tranne primo e ultimo
print(f"tutta la stringa escluso il primo carattere: {s[1:]}") #se non metti il secondo indice arriva fino in fondo
print(f"tutta la stringa escluso l'ultimo carattere: {s[:-1]}") #se non metti il secondo indice arriva fino in fondo
print(s[::-1])# stampa la stringa al contrario da ultimo a primo

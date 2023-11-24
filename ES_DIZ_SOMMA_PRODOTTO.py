#chiedere a utente operazione che si vuole fare, poi i numeri e fare calcolo
def somma(a, b):
    return a+b

def sottrazione(a, b):
    return a-b

def prodotto(a, b):
    return a*b

def divisione(a, b):
    return a/b if b != 0 else "non si puo fare" #non si puo dividere per 0

def main():
    #print(somma)  somma è un oggetto, quindi il codice funziona ma stampa un indirizzo dove si trova la funzione somma
    dizionario = {"+": somma, "*":prodotto, "-":sottrazione, "/":divisione}
    #print(dizionario)
    operazione = input("scrivi '+' per somma e '*' per molti e '/' per div e '-' per sottr: ")
    a = float(input("scrivi il primo numero: "))
    b = float(input("scrivi il secondo numero: "))
    print(dizionario[operazione](a, b))

if __name__ == "__main__":
    main()
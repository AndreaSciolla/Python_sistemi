#LAMBDA FUNCTION: modo utile per definire funzioni brevi

#funzione vecchio stile
'''def somma(a, b):
    return a + b'''

#nuovo costrutto LAMBDA
somma = lambda x, y: x + y #nome funzione = lambda  parametri(separati da virgole): risultato funzione
lista = [10, 4]
x, y = 3, 4

print(somma(x, y))
print(somma(*lista))  #si può spacchettare la lista sui parametri  con *lista  (si può fare solo se lista ha n elementi == n parametri)